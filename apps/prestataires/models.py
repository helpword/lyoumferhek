from django.db import models
from django.contrib.auth import get_user_model
from apps.wilayas.models import Wilaya, Commune


User = get_user_model()

class Prestataire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='prestataire_profile', null=True, blank=True)
    event_types = models.ManyToManyField("events.EventType", verbose_name="Event Types", related_name='prestataires', blank=True)
    name_ar = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.SET_NULL, null=True, blank=True, related_name='prestataires')
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True, blank=True, related_name='prestataires')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_ar} / {self.name_fr}"
