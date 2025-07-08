from django.contrib import admin
from django.urls import path, include
from apps.clients import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', include('home.urls')),  
    path('admin/', admin.site.urls),
    path('client/', include('apps.clients.urls')),
    path('event/', include('apps.events.urls')),
    path('prestataire/', include('apps.prestataires.urls')),
    path('service/', include('apps.services.urls')),
    path('wilaya/', include('apps.wilayas.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
]
