from django.urls import path
from . import views
from .views import prestataire_register_view, prestataire_dashboard

app_name = "prestataires"

urlpatterns = [
    path('register/prestataire/', prestataire_register_view, name='prestataire_register'),
    # path('login/', views.prestataire_login_view, name='prestataire_login'),
    path('dashboard/', prestataire_dashboard, name='prestataire_dashboard'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('add-service/', views.add_service, name='add_service'),
    path('my-services/', views.my_services, name='my_services'),
    path('calendar/', views.calendar_view, name='calendar_view'),
    path('inbox/', views.inbox_view, name='inbox_view'),
]
