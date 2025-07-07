from django.contrib import admin
from .models import Client

admin.site.site_header = "Lyoum Ferhek administration"
admin.site.site_title = "Lyoum Ferhek Admin"
admin.site.index_title = "Lyoum Ferhek Control Panel"

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'birth_date')
    search_fields = ('user__username', 'phone')
