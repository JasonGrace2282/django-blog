from blogauth.models import IonUser
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User


class IonOAuth(BaseBackend):
    def authenticate(self, request, username=None, password=None, *args, **kwargs) -> User | None:
        if (
            username == "admin"
            and password == "testpass123"
            and request.session.get("pk", False)
        ):
            return get_user_by_username(username)
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:  # type: ignore
            return None


def get_user_by_username(username) -> User:
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:  # type: ignore
        user = User(username=username)
        user.is_staff = True  # type: ignore
        user.is_superuser = True  # type: ignore
        user.save()
    return user
