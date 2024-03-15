from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("vous devez entrer un nom d'utilisateur")
        elif len(username) < 4:
            raise ValueError("nom d'utilisateur trop court")
        user = self.model(username=username)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username=username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=50, blank=False, verbose_name="Nom d'utilisateur")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    objects = MyUserManager()

    class Meta:
        verbose_name = "Compte utilisateur"
        verbose_name_plural = "Comptes utilisateurs"


class UserFollows(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="following")
    followed_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="followed_by")

    class Meta:
        unique_together = ("user", "followed_user")
