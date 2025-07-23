# apps/prestataires/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Prestataire
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def create_prestataire_profile(sender, instance, created, **kwargs):
    if created and instance.is_prestataire:
        print("🚨 Signal triggered for prestataire:", instance.email)  # 👈
        Prestataire.objects.create(
            user=instance,
            name_ar=instance.first_name or "nom_ar",
            name_fr=instance.last_name or "nom_fr",
            phone=instance.phone or "0000",
            email=instance.email
        )
