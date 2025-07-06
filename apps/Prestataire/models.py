from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

class Prestataire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='prestataire_profile')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name
