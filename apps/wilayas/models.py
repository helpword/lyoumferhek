from django.db import models
from django.utils import timezone


class Wilaya(models.Model):
    name        = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=255, null=True, blank=True)
    name_fr = models.CharField(max_length=255, null=True, blank=True)
    longitude   = models.FloatField(blank=True, null=True)
    latitude    = models.FloatField(blank=True, null=True)
    code        = models.CharField(max_length=5)
    is_active   = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self):
        return f"{self.code.zfill(2)} - {self.name} ({self.name_fr})"

    class Meta:
        verbose_name = "Wilaya"
        verbose_name_plural = "Wilayas"
        ordering = ['id']




class Commune(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255, null=True, blank=True)
    name_fr = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)  # وأيضًا هذا
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, related_name="communes")
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    is_active   = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    
    def __str__(self):
        return self.name_ar or self.name_fr or self.name


    class Meta:
        ordering = ['name']
