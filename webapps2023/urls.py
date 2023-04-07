from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from register import views as register_views
from userprofile import views as store_views
from notifications import views as notification_views
from currency_exchange.views import ExchangeRate


urlpatterns = [
    path("", store_views.home, name='home'),
    path("transactions/", store_views.past_transactions, name='transactions'),
    path('admin/', admin.site.urls),
    path('edit-info/', store_views.edit_info, name='editInfo'),
    path('register/', register_views.register_user, name='register'),
    path("login/", register_views.login_user, name="login"),
    path("logout/", register_views.logout_user, name="logout"),
    path("transfer/", include('transactions.urls')),
    path("info/", include('miscellaneous.urls')),
    path("send-notifications/", notification_views.send_notifications, name="send_notifications"),
    path("view-notifications/", notification_views.view_notifications, name="view_notifications"),
    path("view-notifications/<int:pk>/", notification_views.mark_read, name="mark_read"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('conversion/<str:convert_from>/<str:convert_to>/', ExchangeRate.as_view(), name="exchange_rate"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

## CHANGE STATIC URLS WHILE DEPLOYING
