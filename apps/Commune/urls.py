from django.urls import path
from . import views

urlpatterns = [
    path('', views.commune_list, name='commune_list'),   
]
