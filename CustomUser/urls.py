from django.urls.conf import path
from .views import user_logout
from .views import SignUpView, UserFollowsView, UnfollowView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", user_logout, name="logout"),
    path("follows/", UserFollowsView.as_view(), name="follows"),
    path("unfollow/<int:pk>/", UnfollowView.as_view(), name="unfollow"),
]
