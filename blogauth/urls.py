from django.urls import path

from .views import login_with_ion, auth_code, authorized_page

urlpatterns = [
    path("", login_with_ion, name='login'),
    path("auth-code", auth_code, name='ion-result'),
    path('authorized', authorized_page, name='authorized')
]
