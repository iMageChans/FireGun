from django.contrib import admin
from node.models import VoteLimit


@admin.register(VoteLimit)
class VoteLimitAdmin(admin.ModelAdmin):
    list_display = ('totals',)