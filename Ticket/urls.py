from django.urls import path
from .views import (
    TicketCreateView,
    TicketUpdateView,
    TicketDeleteView,
    MyPostView,
    ReviewToTicketCreateView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDeleteView,
)


urlpatterns = [
    # Ticket
    path("create/", TicketCreateView.as_view(), name="ticket_create"),
    path("update/<int:pk>/", TicketUpdateView.as_view(), name="ticket_update"),
    path("delete/<int:pk>/", TicketDeleteView.as_view(), name="ticket_delete"),
    # Posts
    path("myposts/", MyPostView.as_view(), name="myposts"),
    # Review
    path("reviewtoticket/<int:pk>/", ReviewToTicketCreateView.as_view(), name="review_create"),
    path("review/", ReviewCreateView.as_view(), name="review_create"),
    path("review/update/<int:pk>/", ReviewUpdateView.as_view(), name="review_update"),
    path("review/delete/<int:pk>/", ReviewDeleteView.as_view(), name="review_delete"),
]
