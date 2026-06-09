from django.contrib import admin
from .models import Ticket, TicketTier, Order, Event
# Register your models here.
admin.site.register(Ticket)
admin.site.register(TicketTier)
admin.site.register(Order)
admin.site.register(Event)