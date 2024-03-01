from django.shortcuts import HttpResponseRedirect, redirect, render
from secrets import CLIENT_ID, CLIENT_SECRET
from requests_oauthlib import OAuth2Session
from config import BlogConfig, AdminProfile


def add_to_base_url(url, **kwargs):
    if kwargs:
        url += "?"

    for k, v in kwargs.items():
        url += f"{k}={v}&"

    return url.rstrip("&")


def login_with_ion(request):
    if BlogConfig.admin_data is not None:
        return authorized_page(request)
    kwargs = {
        "client_id": CLIENT_ID,
        "response_type": "code"
    }
    url = "https://ion.tjhsst.edu/oauth/authorize/"

    return redirect(add_to_base_url(url, **kwargs))


def auth_code(request):
    code = request.GET.get("code", None)
    if code is None:
        return render(
            request,
            'failed.html',
            {"description": "Did you prevent Ion access?"}
        )
    url = "https://ion.tjhsst.edu/oauth/token/"
    kwargs = {
        'code': code,
        'client_secret': CLIENT_SECRET
    }
    oauth = OAuth2Session(
        CLIENT_ID,
        auto_refresh_url=url,
        auto_refresh_kwargs={
            "client_id": CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
    )
    oauth.fetch_token(url, **kwargs)
    profile = oauth.get("https://ion.tjhsst.edu/api/profile")
    BlogConfig.admin_data = AdminProfile(profile.json())
    return HttpResponseRedirect('/admin/authorized')


def authorized_page(request):
    return render(request, 'logged_in.html')
