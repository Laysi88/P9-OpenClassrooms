from django.urls.conf import path
from .views import user_logout
from .views import SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", user_logout, name="logout"),
]
