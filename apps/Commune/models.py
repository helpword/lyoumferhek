from django.db import models
from apps.wilaya.models import Wilaya


class Commune(models.Model):
    wilaya      = models.ForeignKey(Wilaya, on_delete=models.CASCADE, related_name='communes')
    name        = models.CharField(max_length=100)
    post_code   = models.CharField(max_length=6, blank=True, null=True)
    ar_name     = models.CharField(max_length=100, blank=True, null=True)
    longitude   = models.FloatField(blank=True, null=True)
    latitude    = models.FloatField(blank=True, null=True)
    is_active   = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}, {self.wilaya.name}"

    class Meta:
        ordering = ['name']
