from rest_framework import serializers
from decimal import Decimal


class OperationSerializer(serializers.Serializer):
    operation_type = serializers.ChoiceField(choices=['DEPOSIT', 'WITHDRAW'])
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=Decimal('0.01'))
