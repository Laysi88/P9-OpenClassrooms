from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from Ticket.models import Ticket, Review
from CustomUser.models import UserFollows
from django.urls import reverse_lazy
from itertools import chain
from django.db.models import CharField, Value


class Home(LoginRequiredMixin, TemplateView):
    template_name = "LITReview/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = "Flux"
        context["page_name"] = "LitReview"
        context["back_url"] = reverse_lazy("home")

        user_follows = UserFollows.objects.filter(user=self.request.user)
        tickets = Ticket.objects.filter(
            user__in=user_follows.values_list("followed_user", flat=True)
        ) | Ticket.objects.filter(user=self.request.user)
        tickets = tickets.annotate(content_type=Value("ticket", CharField()))

        reviews = (
            Review.objects.filter(ticket__in=tickets)
            | Review.objects.filter(user=self.request.user)
            | Review.objects.filter(ticket__user=self.request.user)
        )
        reviews = reviews.annotate(content_type=Value("review", CharField()))

        # Combiner les tickets et les critiques dans une seule liste
        posts = sorted(chain(tickets, reviews), key=lambda post: post.time_created, reverse=True)

        # pour chaque ticket
        for post in posts:
            if post.content_type == "ticket":
                # on récupère les utilisateurs qui ont commenté
                post.users = Review.objects.filter(ticket=post).values_list("user", flat=True)

        context["posts"] = posts
        return context
