from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.prestataire_register_view, name='prestataire_register'),
    path('ajax/load-services/', views.load_services, name='ajax_load_services'), 
]
