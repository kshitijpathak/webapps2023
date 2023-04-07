from rest_framework import serializers
from .models import CurrencyExchange


class CurrentRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CurrencyExchange
        fields = ('__all__')