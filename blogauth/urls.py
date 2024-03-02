from django.urls import path
from .views import ion_getcode_auth, code_to_token


urlpatterns = [
    path("login/", ion_getcode_auth, name='login-to-ion'),
    path('login/token-code', code_to_token, name='token')
]
