from django.urls.conf import path, include
from .views import UserCreateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("user/", include("django.contrib.auth.urls")),
    path("ucreate/", UserCreateView.as_view(), name="create_user"),
]
