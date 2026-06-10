from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(blank=True, max_length=500)
    location = models.TextField(blank=False, max_length=800)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title}"

class TicketTier(models.Model):
    TICKET_CHOICES = (
        ('GENERAL_ADMISSION','General Admission'),
        ('VIP', 'VIP Meet and Greet')
    )
    name = models.CharField(max_length=30, choices=TICKET_CHOICES)
    total_capacity = models.IntegerField()
    available_quantity  = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL,null=True, related_name='tiers')

    def __str__(self):
        return f"{self.name} - {self.event}"

class Order(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('FAILED', 'Failed'),
        ('CANCELED', 'Canceled')
    )
    purchaser = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order {self.id} by {self.purchaser.username} for {self.event.title}"


class Ticket(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ticket_tier = models.ForeignKey(TicketTier, on_delete=models.CASCADE)
    ticket_id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False)
    is_scanned = models.BooleanField(default=False)
    def __str__(self):
        return f"Ticket {self.ticket_id} for {self.ticket_tier.name} - {self.order.event.title}"



    