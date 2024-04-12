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
        self.fields["username"].widget.attrs.update(
            {
                "placeholder": "Nom d'utilisateur",
                "aria-label": "Nom d'utilisateur",
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                "placeholder": "Mot de passe",
                "aria-label": "Mot de passe",
            }
        )

        self.fields["password2"].widget.attrs.update(
            {
                "placeholder": "Confirmer le mot de passe",
                "aria-label": "Confirmer le mot de passe",
            }
        )


class UserFollowsForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ["followed_user"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if user:
            followed_users = UserFollows.objects.filter(user=user).values_list("followed_user", flat=True)
            queryset = CustomUser.objects.exclude(pk=user.pk)
            if followed_users:
                # Si l'utilisateur suit déjà d'autres utilisateurs, incluez une option pour les supprimer
                queryset = queryset.exclude(pk__in=followed_users)
                self.fields["followed_user"].widget.attrs["class"] = "form-control"
                self.fields["followed_user"].widget.attrs[
                    "placeholder"
                ] = "Choisir un utilisateur à suivre ou arrêter de suivre"
            self.fields["followed_user"].queryset = queryset
