from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def user_logout(request):
    logout(request)
    return render(request, "registration/logged_out.html", {})
