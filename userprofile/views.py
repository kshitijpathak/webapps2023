from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from .forms import UpdateUserForm
from transactions.models import Balance, TransactionHistory
from notifications.models import Notifications


@csrf_protect
def home(request):
    if request.user.is_authenticated:
        current_user = request.user
        transaction_data = TransactionHistory.objects.filter(name=current_user.id).order_by('-created')
        notification_count = len(Notifications.objects.filter(email=current_user.email))
    else:
        transaction_data = [None]
        notification_count = 0

    if notification_count == 0:
        return render(request, "userprofile/home.html", {"transaction_data": transaction_data})
    else:
        return render(request, "userprofile/home.html", {"transaction_data": transaction_data, "notification_count": notification_count})


# View to show all past transactions. User Filter table here and show all fields.
@csrf_protect
def past_transactions(request):
    if request.user.is_authenticated:
        current_user = request.user
        transaction_data = TransactionHistory.objects.filter(name=current_user.id).order_by('-created')
        current_bal = Balance.objects.filter(name=current_user.id)
    else:
        transaction_data = [None]
    return render(request, "transactions/transactions.html", {"transaction_data": transaction_data, "current_bal": current_bal[0]})


# View function to update user information
@csrf_protect
def edit_info(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='editInfo')
    else:
        user_form = UpdateUserForm(instance=request.user)
    return render(request, 'userprofile/myaccount.html', {'user_form': user_form})
