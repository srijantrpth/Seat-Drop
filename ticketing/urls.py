from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TicketTierSet, EventViewSet
from .views import CheckoutView
router = DefaultRouter()
router.register(r'tickettier',TicketTierSet, basename='tickettier')
router.register(r'events',EventViewSet, basename='events')


urlpatterns = [
    path('',include(router.urls)),
    path('checkout/',CheckoutView.as_view(), name='checkout')
]