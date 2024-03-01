from django.urls import path

from .views import login_with_ion, AuthResult

urlpatterns = [
    path("", login_with_ion, name='login'),
    path("auth-code", AuthResult.as_view(), name='ion-result')
]
