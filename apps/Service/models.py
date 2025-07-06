from django.db import models
from ServiceCategory.models import ServiceCategory
from Prestataire.models import Prestataire

class Service(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    prestataire = models.ForeignKey(Prestataire, on_delete=models.CASCADE, related_name='services')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['category', 'name']
