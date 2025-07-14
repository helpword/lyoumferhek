from django.contrib import admin
from .models import Commune, Wilaya

@admin.register(Wilaya)
class WilayaAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'name_fr', 'ar_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'ar_name','name_fr', 'code')

@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ('name', 'wilaya', 'post_code', 'is_active')
    list_filter = ('wilaya', 'is_active')
    search_fields = ('name', 'ar_name', 'name_fr', 'post_code')