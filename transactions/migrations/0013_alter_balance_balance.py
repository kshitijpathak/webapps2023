# Generated by Django 4.1.6 on 2023-04-06 15:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0012_alter_transactionhistory_clearing_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
