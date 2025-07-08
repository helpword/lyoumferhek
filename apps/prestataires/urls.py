from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.prestataire_dashboard, name='prestataire_dashboard'),
]
