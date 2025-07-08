from django.db import models
from apps.wilayas.models import Commune
from apps.clients.models import Client
from django.utils import timezone

from apps.services.models import Service




class EventType(models.Model):
    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100, verbose_name="الاسم بالعربية", null=True, blank=True)
    name_fr = models.CharField(max_length=100, verbose_name="Nom en français", null=True, blank=True)
    



    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name_ar} / {self.name_fr}"

    class Meta:
        verbose_name = "Event Type"
        verbose_name_plural = "Event Types"


class Event(models.Model):
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='events')
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE, related_name='events')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField()

    def __str__(self):
        return f"Event #{self.id} for {self.client}"

    class Meta:
        ordering = ['-created_at']




class EventItem(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='items')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)  # 0-5 rating
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='pending')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.service.name}"

    class Meta:
        unique_together = ('event', 'service')
