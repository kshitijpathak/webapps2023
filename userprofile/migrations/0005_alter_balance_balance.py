# Generated by Django 4.1.6 on 2023-03-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_alter_balance_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='balance',
            field=models.IntegerField(),
        ),
    ]
