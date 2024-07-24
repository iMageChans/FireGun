from django.contrib import admin
from voting.models import Ranks


@admin.register(Ranks)
class RanksAdmin(admin.ModelAdmin):
    list_display = ('node_id', 'node_name', 'sharing_percent', 'accumulative_votes')
    search_fields = ['node_id', 'node_name']
