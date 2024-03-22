from django.urls import path
from .views import TicketCreateView, TicketUpdateView, TicketDeleteView, MyPostView


urlpatterns = [
    # Ticket
    path("create/", TicketCreateView.as_view(), name="ticket_create"),
    path("update/<int:pk>/", TicketUpdateView.as_view(), name="ticket_update"),
    path("delete/<int:pk>/", TicketDeleteView.as_view(), name="ticket_delete"),
    # Posts
    path("myposts/", MyPostView.as_view(), name="myposts"),
]
