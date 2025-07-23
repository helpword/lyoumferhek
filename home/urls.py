from django.urls import path
from .views import home_view, select_event_type, select_venue_type, get_communes
from apps.clients.views import client_login_view, client_register_view
# from apps.prestataires.views import prestataire_login_view, prestataire_register_view

urlpatterns = [
    path('', home_view, name='home'),
    path('select-event/', select_event_type, name='select_event_type'),
    path('select-venue/<str:event_type>/', select_venue_type, name='select_venue_type'),
    path('login/client/', client_login_view, name='client_login'),
    # path('login/prestataire/', prestataire_login_view, name='prestataire_login'),
    path('register/client/', client_register_view, name='client_register'),
    path('get_communes/', get_communes, name='get_communes'),
]
