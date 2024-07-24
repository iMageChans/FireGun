from django.contrib import admin
from mining.models import AccumulativeRewardPool, MerchantVolume, TotalVolume


@admin.register(AccumulativeRewardPool)
class AccumulativeRewardPoolAdmin(admin.ModelAdmin):
    list_display = ('totals',)


@admin.register(MerchantVolume)
class MerchantVolumeAdmin(admin.ModelAdmin):
    list_display = ('totals',)


@admin.register(TotalVolume)
class TotalVolumeAdmin(admin.ModelAdmin):
    list_display = ('totals',)
