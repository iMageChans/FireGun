from django.contrib import admin
from users_profile.models import UserBurningProfile


@admin.register(UserBurningProfile)
class UserBurningProfileAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'amount_burned', 'balance_due', 'balance_paid', 'last_withdrawal', 'last_burn')
    search_fields = ['account_id']

