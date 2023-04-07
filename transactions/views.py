import datetime
import decimal
import random
import requests

from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

from . import models as transact_models
from transactions.forms import TransactionForm
from notifications.models import Notifications


# using decorator for implementing atomicity. Keep this and remove context manager.
@csrf_protect
def send_money(request, pk):
    src_username = request.user.username
    src_bal = transact_models.Balance.objects.select_related().get(name__username=src_username)

    # Using session information - POST-Redirect-GET-Refresh method to prevent duplicated action when
    # user hits refresh after POST request Redirect to GET-View
    if request.session.get('transaction_successful', False):
        request.session['transaction_successful'] = False
        return redirect(request.path)

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            dst_username = form.cleaned_data["enter_destination_username"]
            if src_username == dst_username:
                messages.error(request, "Can not transfer to own account. Please check details..!!")
            elif src_bal.balance < form.cleaned_data["enter_amount_to_transfer"]:
                messages.error(request, "Insufficient Balance. Please verify details...!!")
            else:
                try:
                    # Using context manager for implementing atomicity
                    amount_to_transfer = form.cleaned_data["enter_amount_to_transfer"]
                    dst_bal = transact_models.Balance.objects.select_related().get(name__username=dst_username)
                    if src_bal.currency != dst_bal.currency:
                        r = requests.get(f"http://127.0.0.1:8000/conversion/{src_bal.currency}/{dst_bal.currency}")
                        print(r.json())
                        amount_to_transfer_conv = amount_to_transfer * decimal.Decimal(r.json()[0]['exchange_rate'])
                    else:
                        amount_to_transfer_conv = amount_to_transfer

                    with transaction.atomic():
                        # Updating balances
                        src_bal.balance = src_bal.balance - amount_to_transfer
                        src_bal.save()

                        dst_bal.balance = dst_bal.balance + amount_to_transfer_conv
                        dst_bal.save()

                        # Updating transactions History
                        transfer_comment = form.cleaned_data["enter_comment"]
                        sender_instance = User(id=request.user.id)
                        sender_entry = transact_models.TransactionHistory(name=sender_instance, to_from=dst_username,
                                                                          date=datetime.datetime.now(),
                                                                          transaction_type="sent",
                                                                          amount=amount_to_transfer,
                                                                          clearing_balance=src_bal.balance,
                                                                          comment=transfer_comment)
                        sender_entry.save()

                        receiver_instance = User.objects.filter(username=dst_username)[0]
                        receiver_entry = transact_models.TransactionHistory(name=receiver_instance,
                                                                            to_from=src_username,
                                                                            date=datetime.datetime.now(),
                                                                            transaction_type="received",
                                                                            amount=amount_to_transfer,
                                                                            clearing_balance=dst_bal.balance,
                                                                            comment=transfer_comment)
                        receiver_entry.save()

                        # Modify the on_commit to send confirmation email
                        # subject = "Transaction Successful"
                        # body = form.cleaned_data['enter_comment']
                        # sender = settings.EMAIL_HOST_USER
                        # recipients = receiver_instance.email
                        # password = settings.EMAIL_HOST_PASSWORD
                        # transaction.on_commit(partial(user_message, subject=subject, body=body, sender=sender,
                        #                               recipients=recipients, password=password))

                        request.session['transaction_successful'] = True
                        today = datetime.datetime.now()
                        return render(request, "transactions/sentconfirm.html",
                                      {"payment_ID": random.randint(100000, 999999),
                                       "date": today.strftime("%B %d, %Y at %H:%M:%S"),
                                       "transfer_amount": amount_to_transfer, "src_bal": src_bal, "dst_bal": dst_bal})
                except NameError:
                    messages.error(request, "Destination account does not exists. Please verify details..!!")
        else:
            messages.error(request, "Form is Invalid. Please check values entered!!")
    else:
        if pk > 0:
            notification = Notifications.objects.filter(pk=pk)[0]
            form = TransactionForm(initial={"enter_destination_username": notification.from_user,
                                            "enter_amount_to_transfer": notification.request_amount})
        else:
            form = TransactionForm()
    return render(request, "transactions/sendmoney.html", {"form": form, "src_bal": src_bal})
