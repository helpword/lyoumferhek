from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('', include('home.urls')),  
    path('admin/', admin.site.urls),
    path('client/', include('apps.clients.urls')),
    path('event/', include('apps.events.urls')),
    path('prestataires/', include(('apps.prestataires.urls', 'prestataire'), namespace='prestataire')),
    path('service/', include('apps.services.urls')),
    path('wilaya/', include('apps.wilayas.urls')),
    path('accounts/', include('allauth.urls')),
    path('users/', include('apps.users.urls')),
    path('services/', include('apps.services.urls')),
    path('reviews/', include('apps.reviews.urls')),

    

    # path('prestataire/login/', views.prestataire_login, name='prestataire_login')

] + debug_toolbar_urls()





