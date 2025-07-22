from django.urls import path
from . import views

urlpatterns = [
    path('register/prestataire/', views.prestataire_register, name='prestataire_register'),
    path('ajax/load-services/', views.load_services, name='ajax_load_services'),
]
