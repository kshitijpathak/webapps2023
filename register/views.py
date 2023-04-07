from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect

from .forms import RegisterForm


@csrf_protect
def register_user(request):
    if request.method == 'POST':
        UserForm = RegisterForm(request.POST)
        if UserForm.is_valid():
            # save form and redirect to homepage
            UserForm.save()
            messages.success(request, 'User created. Continue to login..!!')
            return render(request, "userprofile/home.html")
        else:
            # Error Message
            messages.error(request, 'Form is Invalid..!!')
            return render(request, "register/register.html", {"register_user": UserForm})
    else:
        # Render empty form in register template
        UserForm = RegisterForm()
        return render(request, "register/register.html", {"register_user": UserForm})


@csrf_protect
def login_user(request):
    if request.method == 'POST':
        UserForm = AuthenticationForm(data=request.POST)
        if UserForm.is_valid():
            username = UserForm.cleaned_data.get('username')
            password = UserForm.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user, backend=None)
                messages.success(request, f'Welcome {username}, you are logged in..!!')
                return redirect('/')
            else:
                messages.error(request, 'Check the credentials. User does not exist..!!')
                return render(request, "register/login.html", {"login_user": UserForm})
        else:
            return render(request, "register/login.html", {"login_user": UserForm})
    else:
        # Render empty form in register template
        UserForm = AuthenticationForm()
        return render(request, "register/login.html", {"login_user": UserForm})

@csrf_protect
def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful..!!")
    return redirect('/')
