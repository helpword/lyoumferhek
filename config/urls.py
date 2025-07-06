from django.contrib import admin
from django.urls import path, include
from apps.client import views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    
    path('client/', include('apps.client.urls')),
    path('commune/', include('apps.commune.urls')),
    path('event/', include('apps.event.urls')),
    path('eventitems/', include('apps.eventitem.urls')),
    path('eventtype/', include('apps.eventtype.urls')),
    path('prestataire/', include('apps.prestataire.urls')),
    path('service/', include('apps.service.urls')),
    path('service-categories/', include('apps.servicecategory.urls')),
    path('wilaya/', include('apps.wilaya.urls')),
]