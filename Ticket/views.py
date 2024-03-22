from .models import Ticket
from CustomUser.models import CustomUser
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from .forms import TicketForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q


@method_decorator(login_required, name="dispatch")
class TicketCreateView(CreateView):
    """Create a new ticket."""

    model = Ticket
    form_class = TicketForm
    template_name = "ticket/ticket_create.html"
    success_url = reverse_lazy("myposts")

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


@method_decorator(login_required, name="dispatch")
class TicketUpdateView(UpdateView):
    """Update a ticket."""

    model = Ticket
    form_class = TicketForm
    template_name = "ticket/ticket_create.html"
    success_url = reverse_lazy("myposts")

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = "Ticket"
        context["page_name"] = "Modifier un ticket"
        context["submit"] = "Modifier le ticket"
        return context


@method_decorator(login_required, name="dispatch")
class TicketDeleteView(DeleteView):
    """Delete a ticket."""

    model = Ticket
    template_name = "ticket/ticket_delete.html"
    success_url = reverse_lazy("myposts")

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = "Ticket"
        context["page_name"] = "Supprimer un ticket"
        context["submit"] = "Supprimer le ticket"
        return context


@method_decorator(login_required, name="dispatch")
class MyPostView(TemplateView):
    template_name = "ticket/my_posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = "Ticket"
        context["page_name"] = "Mes posts"
        context["tickets"] = Ticket.objects.filter(user=self.request.user)
        return context
