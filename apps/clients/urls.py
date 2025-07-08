
from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),  # قائمة الزبائن (API أو View)
    path('<int:pk>/', views.client_detail, name='client_detail'),  # تفاصيل زبون
    path('dashboard/', views.client_dashboard, name='client_dashboard'),  # لوحة تحكم الزبون
]
