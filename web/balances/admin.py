from django.contrib import admin
from balances.models import *


@admin.register(D9Balance)
class D9BalanceAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'balance_d9')
    search_fields = ['account_id']
