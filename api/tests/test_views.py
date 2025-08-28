import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from decimal import Decimal
import uuid

from api.models import Wallet


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def wallet(db):
    return Wallet.objects.create(id=uuid.uuid4(), balance=Decimal('100.00'))


@pytest.mark.django_db
class TestWalletViews:
    def test_get_wallet_success(self, api_client, wallet):
        response = api_client.get(reverse('wallet', kwargs={'wallet_id': str(wallet.id)}))
        assert response.status_code == 200
        assert response.data['wallet_uuid'] == str(wallet.id)
        assert response.data['balance'] == str(wallet.balance)

    def test_get_wallet_not_found(self, api_client):
        response = api_client.get(reverse('wallet', kwargs={'wallet_id': uuid.uuid4()}))
        assert response.status_code == 404


@pytest.mark.django_db
class TestWalletOperationsView:
    def test_deposit_success(self, api_client, wallet):
        data = {'operation_type': 'DEPOSIT', 'amount': Decimal('50.00')}
        response = api_client.post(
            reverse('wallet_operation', kwargs={'wallet_id': str(wallet.id)}),
            data=data,
            format='json'
        )
        wallet.refresh_from_db()
        assert response.status_code == 200
        assert response.data['info'] == 'Операция успешна!'
        assert wallet.balance == Decimal('150.00')

    def test_withdraw_success(self, api_client, wallet):
        data = {'operation_type': 'WITHDRAW', 'amount': Decimal('50.00')}
        response = api_client.post(
            reverse('wallet_operation', kwargs={'wallet_id': str(wallet.id)}),
            data=data,
            format='json'
        )
        wallet.refresh_from_db()
        assert response.status_code == 200
        assert response.data['info'] == 'Операция успешна!'
        assert wallet.balance == Decimal('50.00')

    def test_invalid_operation_type(self, api_client, wallet):
        data = {'operation_type': 'INVALID', 'amount': Decimal('50.00')}
        response = api_client.post(
            reverse('wallet_operation', kwargs={'wallet_id': str(wallet.id)}),
            data=data,
            format='json'
        )
        wallet.refresh_from_db()
        assert response.status_code == 400
        assert 'operation_type' in response.data
        assert wallet.balance == Decimal('100.00')

    def test_invalid_amount(self, api_client, wallet):
        data = {'operation_type': 'DEPOSIT', 'amount': Decimal('-50.00')}
        response = api_client.post(
            reverse('wallet_operation', kwargs={'wallet_id': str(wallet.id)}),
            data=data,
            format='json'
        )
        wallet.refresh_from_db()
        assert response.status_code == 400
        assert 'amount' in response.data
        assert wallet.balance == Decimal('100.00')

    def test_wallet_not_found(self, api_client):
        data = {'operation_type': 'DEPOSIT', 'amount': Decimal('50.00')}
        response = api_client.post(
            reverse('wallet_operation', kwargs={'wallet_id': uuid.uuid4()}),
            data=data,
            format='json'
        )
        assert response.status_code == 404
