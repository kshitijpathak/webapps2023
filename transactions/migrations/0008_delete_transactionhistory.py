# Generated by Django 4.1.6 on 2023-04-01 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_rename_transactiontype_transactionhistory_transaction_type_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TransactionHistory',
        ),
    ]
