from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Wallet
from .serializer import OperationSerializer


class WalletView(APIView):
    def get(self, request, wallet_id):
        wallet = get_object_or_404(Wallet, id=wallet_id)
        return Response({
            'wallet_uuid': str(wallet.id),
            'balance': str(wallet.balance),
        })
