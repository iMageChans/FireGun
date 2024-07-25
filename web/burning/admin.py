from django.contrib import admin
from burning.models import BurningTotal

@admin.register(BurningTotal)
class BurningTotalAdmin(admin.ModelAdmin):
    list_display = ('totals', )
