from transactions.models import MoneyTransfer
from django import forms


class TransactionForm(forms.ModelForm):

    class Meta:
        model = MoneyTransfer
        fields = ["enter_destination_username", "enter_amount_to_transfer", "enter_comment"]
