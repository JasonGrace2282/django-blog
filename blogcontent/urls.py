from django.urls import path
from .views import BlogView, create_view

urlpatterns = [
    path("", BlogView.as_view(), name='blog'),
    path('create', create_view, name='create')
]
