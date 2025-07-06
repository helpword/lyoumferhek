from django.contrib import admin
from .models import Commune

@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ('name', 'wilaya', 'postal_code', 'is_active')
    list_filter = ('wilaya', 'is_active')
    search_fields = ('name', 'name_ar', 'postal_code')
