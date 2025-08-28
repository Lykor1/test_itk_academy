from django.db import models
import uuid


class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Баланс')

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
