from rest_framework import serializers

from .models import Event, TicketTier
class TicketTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketTier
        fields = '__all__'
    

class EventSerializer(serializers.ModelSerializer):
    tiers = TicketTierSerializer(many=True,read_only=True)
    
    
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'location', 'start_time', 'end_time', 'is_published', 'tiers']        
        
        
class CheckoutSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1, max_value=10)
    tier_id = serializers.IntegerField()