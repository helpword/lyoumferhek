from django.db import models

class Wilaya(models.Model):
    name        = models.CharField(max_length=100)
    ar_name     = models.CharField(max_length=100, blank=True, null=True)
    longitude   = models.FloatField(blank=True, null=True)
    latitude    = models.FloatField(blank=True, null=True)
    code        = models.CharField(max_length=5)
    is_active   = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code.zfill(2)} - {self.name}"

    class Meta:
        verbose_name = "Wilaya"
        verbose_name_plural = "Wilayas"
        ordering = ['id']
