from django.db import models


class CurrencyExchange(models.Model):
    choices = {
        ("GBP", "GBP"),
        ("USD", "USD"),
        ("EUR", "EUR"),
    }
    convert_from = models.CharField(max_length=3, choices=choices)
    convert_to = models.CharField(max_length=3, choices=choices)
    exchange_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.convert_from},{self.convert_to},{self.exchange_rate}"
