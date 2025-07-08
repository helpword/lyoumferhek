from django.contrib import admin
from .models import Commune, Wilaya

@admin.register(Wilaya)
class WilayaAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'name_fr', 'name_ar', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'name_ar','name_fr', 'code')

@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ('name', 'wilaya', 'postal_code', 'is_active')
    list_filter = ('wilaya', 'is_active')
    search_fields = ('name', 'name_ar', 'name_fr', 'postal_code')