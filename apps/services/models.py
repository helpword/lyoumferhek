from django.db import models
from django.conf import settings
from apps.prestataires.models import Prestataire




class ServiceCategory(models.Model):
    name_ar = models.CharField(max_length=100, null=True, blank=True)
    name_fr = models.CharField(max_length=100, null=True, blank=True)
    event_types = models.ManyToManyField("events.EventType", verbose_name="Event Types", related_name='service_categories')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_ar} / {self.name_fr}"

    class Meta:
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"



class Service(models.Model):
    name_ar = models.CharField(max_length=100, null=True, blank=True)
    name_fr = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    event_types = models.ManyToManyField("events.EventType", verbose_name="Event Types", related_name='services')
    prestataire = models.ForeignKey(Prestataire, on_delete=models.CASCADE, related_name='services')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_ar} / {self.name_fr}"

    class Meta:
        ordering = ['category', 'name_ar', 'name_fr']

class Order(models.Model):
    prestataire = models.ForeignKey("prestataires.Prestataire", on_delete=models.CASCADE, related_name="orders")
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ("en_attente", "En attente"),
        ("confirme", "Confirmé"),
        ("annule", "Annulé"),
    ])
    # أضف أي حقول أخرى حسب الحاجة

    def __str__(self):
        return f"Commande pour {self.prestataire.name_fr} - {self.status}"

