from django.db import models
from Commune.models import Commune
from Client.models import Client
from EventType.models import EventType

class Event(models.Model):
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='events')
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE, related_name='events')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()

    def __str__(self):
        return f"Event #{self.id} for {self.client}"

    class Meta:
        ordering = ['-created_at']
