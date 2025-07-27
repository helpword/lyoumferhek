from django.urls import path
from . import views

urlpatterns = [
    path('prestataire/<int:prestataire_id>/review/', views.leave_review, name='leave_review'),
]
