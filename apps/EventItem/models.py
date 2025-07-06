from django.db import models
from Event.models import Event
from Service.models import Service

class EventItem(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='items')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)  # 0-5 rating
    comment = models.TextField(blank=True, null=True)
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
