from django.urls import path

from .views import LoggedIn, make_auth

urlpatterns = [
    path("", make_auth, name="auth"),
    path("loggedin", LoggedIn.as_view(), name="loggedin")
]
