from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ✅ هذا يعرض الصفحة الرئيسية
    path('step1/', views.step1_view, name='step1'),
    path('step2/', views.step2_view, name='step2'),
    path('step3/', views.step3_view, name='step3'),
    path('step4/', views.step4_view, name='step4'),
    path('complete/', views.form_complete_view, name='form_complete'),
]
