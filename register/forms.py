from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from transactions.models import Balance
import requests


# User Registration Form
class RegisterForm(UserCreationForm):
    CURRENCY = [
        ('GBP', 'British Pounds'),
        ('USD', 'US Dollars'),
        ('EUR', 'Euros')
    ]

    email = forms.EmailField()
    currency = forms.CharField(label='Currency', widget=forms.Select(choices=CURRENCY))

    def save(self, commit=True, *args, **kwargs):
        instance = super(RegisterForm, self).save(*args, **kwargs)
        if self.cleaned_data['currency'] != "GBP":
            r = requests.get(f"http://127.0.0.1:8000/conversion/GBP/{self.cleaned_data['currency']}")
            print(r.json())
            bal = 1000*float(r.json()[0]['exchange_rate'])
            print(bal)
        else:
            bal = 1000

        Balance.objects.create(name=instance, balance=bal, currency=self.cleaned_data['currency'])
        return instance

    class Meta:
        model = User
        fields = ['first_name', 'last_name', "username", "currency", "email", "password1", "password2"]
