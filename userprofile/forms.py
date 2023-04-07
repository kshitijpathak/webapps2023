from django import forms

from django.contrib.auth.models import User


class UpdateUserForm(forms.ModelForm):
    CURRENCY = [
        ('GBP', 'British Pounds'),
        ('USD', 'US Dollars'),
        ('EUR', 'Euros')
    ]

    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True, disabled=True)
    email = forms.EmailField(required=True)
    currency = forms.CharField(label='Currency', widget=forms.Select(choices=CURRENCY))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', "username", "currency", "email"]
