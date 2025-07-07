from django.db import models

from apps.prestataires.models import Prestataire




class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"


class Service(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    prestataire = models.ForeignKey(Prestataire, on_delete=models.CASCADE, related_name='services')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['category', 'name']
