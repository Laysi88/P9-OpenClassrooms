from django.urls.conf import path
from .views import UserCreateView, user_logout


urlpatterns = [
    path("ucreate/", UserCreateView.as_view(), name="create_user"),
    path("logout/", user_logout, name="logout"),
]
