from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Client
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def create_client_profile(sender, instance, created, **kwargs):
    if created and instance.is_client:
        Client.objects.create(user=instance, phone=instance.phone )
