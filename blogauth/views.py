from django.shortcuts import redirect
from django.views.generic import TemplateView
from secrets import CLIENT_ID, CLIENT_SECRET


def login_with_ion(_):
    kwargs = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    url = "https://ion.tjhsst.edu/oauth/authorize/"
    if kwargs:
        url += "?"

    for k, v in kwargs.items():
        url += f"{k}={v}&"

    return redirect(url.rstrip("&"))


class AuthResult(TemplateView):
    template_name = 'auth.html'
