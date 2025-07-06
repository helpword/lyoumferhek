from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'event_type', 'commune', 'date', 'created_at')
    list_filter = ('event_type', 'commune', 'date')
    search_fields = ('client__user__username',)
