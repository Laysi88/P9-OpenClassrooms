from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, UserFollowsForm
from .models import UserFollows


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def user_logout(request):
    logout(request)
    return render(request, "registration/logged_out.html", {})


@method_decorator(login_required, name="dispatch")
class UserFollowsView(CreateView):
    form_class = UserFollowsForm
    model = UserFollows
    template_name = "UserAccount/follows.html"
    success_url = reverse_lazy("follows")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        followed_user = form.cleaned_data["followed_user"]

        existing_follow = UserFollows.objects.filter(user=user, followed_user=followed_user).exists()
        if existing_follow:
            UserFollows.objects.filter(user=user, followed_user=followed_user).delete()
        else:
            form.instance.user = user
            form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["follows"] = UserFollows.objects.filter(user=self.request.user)
        return context
