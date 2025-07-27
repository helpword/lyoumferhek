from django.urls import path
from . import views
from .views import get_communes

urlpatterns = [
    path('', views.wilaya_list, name='wilaya_list'),
    path('', views.commune_list, name='commune_list'),
    path("api/communes/", get_communes),
    # path('<int:pk>/', views.wilaya_detail, name='wilaya_detail'),
]
