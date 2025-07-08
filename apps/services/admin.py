from django.contrib import admin

from .models import  Service, ServiceCategory


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'name_fr', 'category', 'prestataire', 'price')
    list_filter = ('category', 'prestataire')
    search_fields = ('name_ar', 'name_fr', 'category__name_ar', 'category__name_fr', 'prestataire__name_ar', 'prestataire__name_fr')



@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'name_fr', 'created_at', 'updated_at')
