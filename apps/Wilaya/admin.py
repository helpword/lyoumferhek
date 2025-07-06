from django.contrib import admin
from .models import Wilaya

@admin.register(Wilaya)
class WilayaAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'ar_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'ar_name', 'code')
