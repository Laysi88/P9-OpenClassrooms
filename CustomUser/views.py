from .models import CustomUser
from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "UserAccount/create_user.html"
    success_url = reverse_lazy("login")


@login_required
def user_logout(request):
    logout(request)
    return render(request, "registration/logged_out.html", {})
