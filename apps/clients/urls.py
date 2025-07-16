
from django.urls import path
from . import views
from .views import search_services

urlpatterns = [
    path('', views.client_list, name='client_list'),  # قائمة الزبائن (API أو View)
    path('<int:pk>/', views.client_detail, name='client_detail'),  # تفاصيل زبون
    path('dashboard/', views.client_dashboard, name='client_dashboard'),  
    path('search/', search_services, name='search_services'),
    path('client/login/', views.client_login_view, name='client_login'),
    path('client/register/', views.client_register_view, name='client_register'),
    path('client/dashboard/', views.client_dashboard, name='client_dashboard'),

]
