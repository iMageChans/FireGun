from django.contrib import admin
from merchant.models import *


@admin.register(MerchantExpiry)
class MerchantExpiryAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'expiry_date')
    search_fields = ['account_id']
