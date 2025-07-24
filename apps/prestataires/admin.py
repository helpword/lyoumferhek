from django.contrib import admin
from .models import Prestataire

@admin.register(Prestataire)
class PrestataireAdmin(admin.ModelAdmin):
    list_display = ('name_fr', 'email', 'phone', 'wilaya', 'commune', 'is_approved')
    list_filter = ('wilaya', 'commune', 'is_approved')
    search_fields = ('name_fr', 'email', 'phone')
