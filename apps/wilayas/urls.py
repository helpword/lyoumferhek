from django.urls import path
from . import views

urlpatterns = [
    path('', views.wilaya_list, name='wilaya_list'),
    path('', views.commune_list, name='commune_list'),
    # path('<int:pk>/', views.wilaya_detail, name='wilaya_detail'),
]
