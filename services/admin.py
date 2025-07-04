from django.contrib import admin
from .models import EventLocationType  # هذا موجود، فلا مشكلة
admin.site.register(EventLocationType)

from .models import (
    Client, EventType,
    Wilaya, Commune,
    Prestataire, ServiceCategory, Service,
    Order, OrderItem
)

admin.site.register(Client)
admin.site.register(EventType)
admin.site.register(Wilaya)
admin.site.register(Commune)
admin.site.register(Prestataire)
admin.site.register(ServiceCategory)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(OrderItem)
