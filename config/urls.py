from django.contrib import admin
from django.urls import path, include
from apps.clients import views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    
    path('client/', include('apps.clients.urls')),
    path('event/', include('apps.events.urls')),
    path('prestataire/', include('apps.prestataires.urls')),
    path('service/', include('apps.services.urls')),
    path('wilaya/', include('apps.wilayas.urls')),
]