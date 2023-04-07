from django.contrib import admin
from .models import TransactionHistory, Balance

admin.site.register(TransactionHistory)
admin.site.register(Balance)
