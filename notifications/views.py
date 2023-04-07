from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from notifications.forms import RequestMoney
from notifications.models import Notifications


def view_notifications(request):
    unseen_notifications = Notifications.objects.filter(email=request.user.email, is_seen=False)
    seen_notifications = Notifications.objects.filter(email=request.user.email, is_seen=True)
    return render(request, 'notifications/view_notifications.html', {"unseen_notifications": unseen_notifications,
                                                                     "seen_notifications": seen_notifications})


@csrf_protect
def send_notifications(request):
    if request.method == 'POST':
        form = RequestMoney(request.POST, initial={"from_user": request.user})
        # print(form.cleaned_data)
        if form.is_valid():
            request_from = form.cleaned_data['email']
            receiver_instance = User.objects.filter(email__exact=request_from)
            if len(receiver_instance) == 0:
                messages.error(request, "Destination account does not exists. Please verify details..!!")
            elif request.user.email == request_from:
                messages.error(request, "Can not request your own account. Please check details..!!")
            else:
                form.save()
                messages.success(request, 'Request Processed Successfully..!!')
                return redirect(request.path)
        else:
            messages.error(request, "Form is Invalid. Please check values entered!!")
    else:
        form = RequestMoney(initial={"from_user": request.user})
    return render(request, "notifications/send_notifications.html", {"form": form})


@csrf_protect
def mark_read(request, pk):
    notification = Notifications.objects.filter(pk=pk)[0]
    notification.is_seen = True
    notification.save()
    return redirect("view_notifications")
