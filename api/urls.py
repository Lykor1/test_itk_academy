from django.urls import path

from .views import WalletView, WalletOperationsView

urlpatterns = [
    path('wallet/<wallet_id>/', WalletView.as_view(), name='wallet'),
    path('wallet/<wallet_id>/operation/', WalletOperationsView.as_view(), name='wallet_operation'),
]
