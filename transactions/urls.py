from django.urls import path
from . import views

urlpatterns = [
    path("sendmoney/<int:pk>/", views.send_money, name="sendMoney"),
]
