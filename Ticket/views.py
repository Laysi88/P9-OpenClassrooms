from .models import Ticket
from CustomUser.models import CustomUser
from django.views.generic import CreateView
from .forms import TicketForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class TicketCreateView(CreateView):
    """Create a new ticket."""

    model = Ticket
    form_class = TicketForm
    template_name = "ticket/ticket_create.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = "Ticket"
        context["page_name"] = "Créer un ticket"
        context["submit"] = "Créer le ticket"
        return context
