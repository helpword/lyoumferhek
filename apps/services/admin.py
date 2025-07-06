from django.contrib import admin

from .models import (
    Client, EventType,
    Wilaya, Commune,
    Prestataire, ServiceCategory, Service,
    Event, EventItem
)



@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ar_name', 'wilaya', 'post_code', 'is_active')
    list_display_links = ('id', 'name')
    list_editable = ['ar_name', 'wilaya', 'post_code', 'is_active']
    exclude = ['title', 'sub_title']
    list_filter = ['wilaya', 'is_active']




admin.site.register(Client)
admin.site.register(EventType)
admin.site.register(Wilaya)
admin.site.register(Prestataire)
admin.site.register(ServiceCategory)
admin.site.register(Service)
admin.site.register(Event)
admin.site.register(EventItem)
