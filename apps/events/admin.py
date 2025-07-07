from django.contrib import admin
from .models import Event , EventItem, EventType

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'event_type', 'commune', 'date', 'created_at')
    list_filter = ('event_type', 'commune', 'date')
    search_fields = ('client__user__username',)



@admin.register(EventItem)
class EventItemAdmin(admin.ModelAdmin):
    list_display = ('event', 'service', 'quantity', 'status', 'rating')
    list_filter = ('status', 'rating')
    search_fields = ('event__id', 'service__name')



@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
