from django.contrib import admin
from .models import EventItem

@admin.register(EventItem)
class EventItemAdmin(admin.ModelAdmin):
    list_display = ('event', 'service', 'quantity', 'status', 'rating')
    list_filter = ('status', 'rating')
    search_fields = ('event__id', 'service__name')
