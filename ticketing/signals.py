from django.db.models.signals import post_save
from django.dispatch import receiver

from .tasks import send_completion_email
from .models import TicketTier, Event   
from django.db.models import Sum

@receiver(post_save, sender=TicketTier)
def update_event_sold_out_status(sender, instance, **kwargs):
    event = instance.event
    total_remaining = event.tiers.aggregate(total=Sum('available_quantity'))['total'] or 0
    if(total_remaining==0):
        event.is_sold_out = True
        
    else:
        event.is_sold_out = False
    event.save()

   