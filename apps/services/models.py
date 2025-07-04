from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()



# -----------------------
# Services: Prestataire, Category, Service
# -----------------------
class Prestataire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)

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

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['category', 'name']


# -----------------------
# Client
# -----------------------
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

# -----------------------
class EventType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Event Type"
        verbose_name_plural = "Event Types"

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

        
class Commune(models.Model):
    wilaya      = models.ForeignKey(Wilaya, on_delete=models.CASCADE, related_name='communes')
    name        = models.CharField(max_length=100)
    post_code   = models.CharField(max_length=6, blank=True, null=True)
    ar_name     = models.CharField(max_length=100, blank=True, null=True)
    longitude   = models.FloatField(blank=True, null=True)
    latitude    = models.FloatField(blank=True, null=True)
    is_active   = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}, {self.wilaya.name}"

    class Meta:
        ordering = ['name']
# -----------------------
# Order & OrderItem
# -----------------------
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

# -----------------------
# EventType فقط

# -----------------------
# Location: Wilaya & Commune
# -----------------------
