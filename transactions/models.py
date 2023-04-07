from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Model to store current balance of a user
class Balance(models.Model):
    CURRENCY = [
        ('GBP', 'British Pounds'),
        ('USD', 'US Dollars'),
        ('EUR', 'Euros')
    ]

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(0)])
    currency = models.CharField(max_length=3, choices=CURRENCY, default='GBP')

    def __str__(self):
        return f"{self.name}, {self.balance}, {self.currency}"


# Model to keep track of historical transactions. Updates when transactions made
class TransactionHistory(models.Model):
    TYPE = [
        ('sent', 'Sent'),
        ('received', 'Received')
    ]
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    to_from = models.CharField(max_length=100)
    date = models.DateField()
    transaction_type = models.CharField(max_length=8, choices=TYPE)
    amount = models.PositiveIntegerField()
    clearing_balance = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(0)])
    comment = models.CharField(max_length=30, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.to_from}, {self.name}, {self.date}, {self.transaction_type}, {self.amount}, {self.clearing_balance}" \
               f", {self.comment}, {self.created}"


# Model to create transaction Form
class MoneyTransfer(models.Model):
    enter_destination_username = models.CharField(max_length=50)
    enter_amount_to_transfer = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    enter_comment = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.enter_destination_username}, {self.enter_amount_to_transfer}, {self.enter_comment}"
