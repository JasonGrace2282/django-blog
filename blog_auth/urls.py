from django.urls import path

from .views import AuthPage, BlogView

urlpatterns = [
    path("", AuthPage.as_view(), name="auth"),
    path("blog", BlogView.as_view(), name="blog")
]
