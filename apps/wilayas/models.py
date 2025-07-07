from django.db import models
from django.utils import timezone


class Wilaya(models.Model):
    name        = models.CharField(max_length=100)
    ar_name     = models.CharField(max_length=100, blank=True, null=True)
    longitude   = models.FloatField(blank=True, null=True)
    latitude    = models.FloatField(blank=True, null=True)
    code        = models.CharField(max_length=5)
    is_active   = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code.zfill(2)} - {self.name}"

    class Meta:
        verbose_name = "Wilaya"
        verbose_name_plural = "Wilayas"
        ordering = ['id']




class Commune(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    ar_name = models.CharField(max_length=255, blank=True, null=True)  # أضف هذا إن لم يكن موجودًا
    postal_code = models.CharField(max_length=10, blank=True, null=True)  # وأيضًا هذا
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    is_active   = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']
