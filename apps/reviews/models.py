from django.db import models
from apps.clients.models import Client
from apps.prestataires.models import Prestataire

class Review(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="reviews")
    prestataire = models.ForeignKey(Prestataire, on_delete=models.CASCADE, related_name="reviews_reviews")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('client', 'prestataire')  # كل زبون يمكنه تقييم مقدم خدمة مرة واحدة فقط
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client.user.username} rated {self.prestataire.user.username} ({self.rating})"
