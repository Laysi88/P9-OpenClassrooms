from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserFollows
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ajouter des placeholders
        self.fields["username"].widget.attrs["placeholder"] = "Nom d'utilisateur"
        self.fields["password1"].widget.attrs["placeholder"] = "Mot de passe"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirmer le mot de passe"


class UserFollowsForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ["followed_user"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields["followed_user"].queryset = CustomUser.objects.exclude(pk=user.pk)
