from django.db import models
from django.contrib.auth.models import User

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
# Event & EventType
# -----------------------
class EventType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Event Type"
        verbose_name_plural = "Event Types"

class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='events')
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.event_type.name} for {self.client}"

    class Meta:
        ordering = ['-date']

# -----------------------
# Location: Wilaya & Commune
# -----------------------
class Wilaya(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        verbose_name = "Wilaya"
        verbose_name_plural = "Wilayas"
        ordering = ['code']

class Commune(models.Model):
    name = models.CharField(max_length=100)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, related_name='communes')

    def __str__(self):
        return f"{self.name}, {self.wilaya.name}"

    class Meta:
        ordering = ['name']

# -----------------------
# Event Location (Venue)
# -----------------------
class EventLocation(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True, related_name='locations')
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

# -----------------------
# Services: Prestataire, Category, Service
# -----------------------
class Prestataire(models.Model):
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
# Order & OrderItem
# -----------------------
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} for {self.client}"

    class Meta:
        ordering = ['-created_at']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.service.name}"

    class Meta:
        unique_together = ('order', 'service')
