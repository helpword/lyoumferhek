from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

