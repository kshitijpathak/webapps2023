from rest_framework import generics
from .serializers import CurrentRateSerializer
from .models import CurrencyExchange


class ExchangeRate(generics.ListCreateAPIView):
    serializer_class = CurrentRateSerializer

    def get_queryset(self):
        queryset = CurrencyExchange.objects.all()
        queryset = queryset.filter(convert_from=self.kwargs["convert_from"], convert_to=self.kwargs["convert_to"])
        return queryset



