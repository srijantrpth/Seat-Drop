from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Event, TicketTier, Order, Ticket
from .serializers import EventSerializer, TicketTierSerializer, CheckoutSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = CheckoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tier_id = serializer.validated_data.get('tier_id')
        quantity = serializer.validated_data.get('quantity')
        
        try:
            with transaction.atomic():
                tier = TicketTier.objects.select_for_update.get(id=tier_id)
                if not tier.available_quantity >= quantity:
                    return Response({"error": "Unfortunately! Tickets of selected tier are not available! "}, status.HTTP_400_BAD_REQUEST)
                total_price = tier.price*quantity
                order = Order.objects.create(event=tier.event, purchaser=request.user, total_price=total_price, status='PAID')
                tier.available_quantity-=quantity
                tier.save()
                tickets_to_create = [Ticket(order=order, ticket_tier=tier) for _ in range(quantity)]
                Ticket.objects.bulk_create(tickets_to_create)
            return Response({f"message": f"Successfully purchased {quantity} tickets for {tier.event.title} at {total_price}"}, status=status.HTTP_201_CREATED)
            
            
        except TicketTier.DoesNotExist:
            return Response({"error": "The requested ticket tier does not exist! "}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TicketTierSet(viewsets.ModelViewSet):
    queryset = TicketTier.objects.all()
    serializer_class = TicketTierSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

