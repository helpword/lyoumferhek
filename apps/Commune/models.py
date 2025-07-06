from django.db import models
from apps.wilaya.models import Wilaya


class Commune(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255, blank=True, null=True)  # أضف هذا إن لم يكن موجودًا
    postal_code = models.CharField(max_length=10, blank=True, null=True)  # وأيضًا هذا
    wilaya = models.ForeignKey('wilaya.Wilaya', on_delete=models.CASCADE)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    is_active   = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']
