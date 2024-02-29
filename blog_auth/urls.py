from django.urls import path

from .views import home_page_view

urlpatterns = [
    # "" means url/
    # if it was "hi" it would be url/hi
    path("", home_page_view, name="home")
]
