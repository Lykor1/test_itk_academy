from django.urls import path

from .views import WalletView

urlpatterns = [
    path('<wallet_id>/', WalletView.as_view(), name='wallet'),
]
