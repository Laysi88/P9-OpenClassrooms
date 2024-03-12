from .models import CustomUser
from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "UserAccount/create_user.html"
    success_url = reverse_lazy("login")
