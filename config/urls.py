from django.contrib import admin
from django.urls import path, include
from apps.clients import views
from django.contrib.auth import views as auth_views
from apps.clients.views import client_register_view
from apps.prestataires.views import prestataire_register_view
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('', include('home.urls')),  
    path('admin/', admin.site.urls),
    path('client/', include('apps.clients.urls')),
    path('event/', include('apps.events.urls')),
    path('prestataire/', include('apps.prestataires.urls')),
    path('service/', include('apps.services.urls')),
    path('wilaya/', include('apps.wilayas.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('register/client/', client_register_view, name='client_register'),
    path('register/prestataire/', prestataire_register_view, name='prestataire_register'),
    path('accounts/', include('allauth.urls')),
    path('users/', include('apps.users.urls')),
    path('services/', include('apps.services.urls')),
    

    # path('prestataire/login/', views.prestataire_login, name='prestataire_login')

] + debug_toolbar_urls()





