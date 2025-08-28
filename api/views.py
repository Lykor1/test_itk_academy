from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.db.models import F

from .models import Wallet
from .serializer import OperationSerializer


class WalletView(APIView):
    def get(self, request, wallet_id):
        wallet = get_object_or_404(Wallet, id=wallet_id)
        return Response({
            'wallet_uuid': str(wallet.id),
            'balance': str(wallet.balance),
        })


class WalletOperationsView(APIView):
    def post(self, request, wallet_id):
        get_object_or_404(Wallet, id=wallet_id)
        serializer = OperationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        operation = serializer.validated_data['operation_type']
        amount = serializer.validated_data['amount']
        with transaction.atomic():
            if operation == 'DEPOSIT':
                Wallet.objects.filter(id=wallet_id).update(balance=F('balance') + amount)
            else:
                updated = Wallet.objects.filter(id=wallet_id, balance__gte=amount).update(balance=F('balance') - amount)
                if updated == 0:
                    return Response({'error': 'Не хватает средств'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'info': 'Операция успешна!'}, status=status.HTTP_200_OK)
