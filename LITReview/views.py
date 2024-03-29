from CustomUser.utils import CustomLoginRequired
from django.views.generic import TemplateView
from Ticket.models import Ticket, Review
from CustomUser.models import UserFollows
from django.urls import reverse_lazy


class Home(CustomLoginRequired, TemplateView):
    template_name = "LITReview/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # General parameter of the page
        context["app_name"] = "Flux"
        context["page_name"] = "LitReview"
        context["back_url"] = reverse_lazy("home")

        user_follows = UserFollows.objects.filter(user=self.request.user)

        # récuperer les tickets des utilisateurs suivis
        tickets = Ticket.objects.filter(
            user__in=user_follows.values_list("followed_user", flat=True)
        ) | Ticket.objects.filter(user=self.request.user)
        context["tickets"] = tickets

        # récuperer les reviews des utilisateurs suivis ou de l'utilisateur ou des tickets créés par l'utilisateur
        reviews = (
            Review.objects.filter(ticket__in=tickets)
            | Review.objects.filter(user=self.request.user)
            | Review.objects.filter(ticket__user=self.request.user)
        )
        context["reviews"] = reviews

        return context
