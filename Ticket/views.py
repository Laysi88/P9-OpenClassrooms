from .models import Ticket, Review
from CustomUser.models import CustomUser
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, FormView
from .forms import TicketForm, ReviewToTIcketForm, ReviewForm
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
class ReviewToTicketCreateView(CreateView):
    """Create a new review."""

    model = Review
    form_class = ReviewToTIcketForm
    template_name = "ticket/reviewtoticket_create.html"
    success_url = reverse_lazy("myposts")

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.ticket = Ticket.objects.get(pk=self.kwargs["pk"])
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ticket"] = Ticket.objects.get(pk=self.kwargs["pk"])
        context["app_name"] = "Avis"
        context["page_name"] = "Créer une critique"
        context["submit"] = "Créer la critique"
        return context


@method_decorator(login_required, name="dispatch")
class ReviewCreateView(FormView):
    """Create ticket and review."""

    form_class = ReviewForm
    template_name = "ticket/review_create.html"
    success_url = reverse_lazy("myposts")

    def form_valid(self, form):
        form.instance.user = self.request.user
        ticket = Ticket.objects.create(
            title=form.cleaned_data["title"],
            description=form.cleaned_data["description"],
            image=form.cleaned_data["image"],
            user=self.request.user,
        )
        Review.objects.create(
            headline=form.cleaned_data["headline"],
            body=form.cleaned_data["body"],
            rating=form.cleaned_data["rating"],
            ticket=ticket,
            user=self.request.user,
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = "Avis"
        context["page_name"] = "Créer une critique"
        context["submit"] = "Créer la critique"
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
class ReviewUpdateView(UpdateView):
    """Update a review."""

    model = Review
    form_class = ReviewToTIcketForm
    template_name = "ticket/review_create.html"
    success_url = reverse_lazy("myposts")

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = "Avis"
        context["page_name"] = "Modifier un avis"
        context["submit"] = "Modifier l'avis"
        return context


@method_decorator(login_required, name="dispatch")
class ReviewDeleteView(DeleteView):
    """Delete a review."""

    model = Review
    template_name = "ticket/review_delete.html"
    success_url = reverse_lazy("myposts")

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = "Avis"
        context["page_name"] = "Supprimer une critique"
        context["submit"] = "Supprimer la critique"
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
        context["reviews"] = Review.objects.filter(user=self.request.user)
        return context
