from django.contrib import admin
from .models import (
    Client, EventType, Event,
    Wilaya, Commune, EventLocation,
    Prestataire, ServiceCategory, Service,
    Order, OrderItem
)

# Titre principal en haut de la page d'administration
admin.site.site_header = "Panneau d'administration Lyoum Ferhek"

# Titre de l'onglet dans le navigateur
admin.site.site_title = "Gestion du Lyoum Ferhek"

# Titre de la page d'accueil du panneau d'administration
admin.site.index_title = "Bienvenue dans le panneau d'administration Lyoum Ferhek"
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
