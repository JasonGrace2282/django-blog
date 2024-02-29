from django.urls import path

from .views import HomePageView, AboutView

urlpatterns = [
    # "" means url/
    # if it was "hi" it would be url/hi
    path("", HomePageView.as_view(), name="home"),
    path("about", AboutView.as_view(), name="about")
]
