from CustomUser.utils import CustomLoginRequired
from django.views.generic import TemplateView
from django.urls import reverse_lazy


class Home(CustomLoginRequired, TemplateView):
    template_name = "LITReview/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # General parameter of the page
        context["app_name"] = "Flux"
        context["page_name"] = "LitReview"
        context["back_url"] = reverse_lazy("home")

        return context
