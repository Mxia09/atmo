from django.urls import path
from accounts.views import user_logout

urlpatterns = [
    path("logout/", user_logout, name="logout"),
]