from django.contrib import admin

from .models import Wallet


# admin.site.register(Wallet)
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('id',)
