from django.urls import path
from .views import TicketCreateView, TicketUpdateView


urlpatterns = [
    # Ticket
    path("create/", TicketCreateView.as_view(), name="ticket_create"),
    path("update/<int:pk>/", TicketUpdateView.as_view(), name="ticket_update"),
]
