from django.urls import path
from accounts.views import user_logout, user_login, user_signup

urlpatterns = [
    path("logout/", user_logout, name="logout"),
    path("login/", user_login, name="login"),
    path("signuo/", user_signup, name="signup")
]