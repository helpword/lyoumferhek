from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'prestataire', 'price')
    list_filter = ('category', 'prestataire')
    search_fields = ('name',)
