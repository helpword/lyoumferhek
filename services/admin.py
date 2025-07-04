from django.contrib import admin
from .models import (
    Client, EventType, Event,
    Wilaya, Commune, EventLocation,
    Prestataire, ServiceCategory, Service,
    Order, OrderItem
)

# Register your models here.
admin.site.register(Client)
admin.site.register(EventType)
admin.site.register(Event)
admin.site.register(Wilaya)
admin.site.register(Commune)
admin.site.register(EventLocation)
admin.site.register(Prestataire)
admin.site.register(ServiceCategory)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(OrderItem)
