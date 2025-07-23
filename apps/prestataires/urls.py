from django.urls import path
from . import views
from .views import prestataire_register_view
from .views import prestataire_dashboard




urlpatterns = [
    path('register/prestataire/', prestataire_register_view, name='prestataire_register'),
    path('login/', views.prestataire_login_view, name='prestataire_login'),
    path('dashboard/', prestataire_dashboard, name='prestataire_dashboard'),

]
