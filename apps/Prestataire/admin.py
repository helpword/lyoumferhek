from django.contrib import admin
from .models import Prestataire

@admin.register(Prestataire)
class PrestataireAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'phone', 'email')
    search_fields = ('name', 'user__username')
