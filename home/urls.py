from django.urls import path
from .views import home_view, select_event_type, select_venue_type

urlpatterns = [
    path('', home_view, name='home'),
    path('select-event/', select_event_type, name='select_event_type'),
    path('select-venue/<str:event_type>/', select_venue_type, name='select_venue_type'),
]
