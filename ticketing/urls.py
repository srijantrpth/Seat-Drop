from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TicketTierSet, EventViewSet
router = DefaultRouter()
router.register(r'tickettier',TicketTierSet, basename='tickettier')
router.register(r'events',EventViewSet, basename='events')


urlpatterns = [
    path('',include(router.urls))
]