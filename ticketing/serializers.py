from rest_framework import serializers

from .models import Event, TicketTier
class TicketTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketTier
        
        fields = '__all__'
    

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        tiers = TicketTierSerializer(many=True, read_only=True)
        
        
    

