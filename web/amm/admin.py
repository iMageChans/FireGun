from django.contrib import admin
from .models import CurrencyReserves, ExchangeRate


@admin.register(CurrencyReserves)
class CurrencyReservesAdmin(admin.ModelAdmin):
    list_display = ('d9', 'usdt', 'd9_to_usdt', 'usdt_to_d9')
    search_fields = ['d9', 'usdt']


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('d9', 'usdt')
    search_fields = ['d9', 'usdt']
