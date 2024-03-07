from django.shortcuts import redirect, render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from requests_oauthlib import OAuth2Session
from .models import BlogConfig
import os
import json


CLIENT_ID = os.environ["BLOG_ION_CLIENT_ID"]
CLIENT_SECRET = os.environ["BLOG_ION_CLIENT_SECRET"]

authorize_url = "https://ion.tjhsst.edu/oauth/authorize/"
token_url = "https://ion.tjhsst.edu/oauth/token/"
profile_url = "https://ion.tjhsst.edu/api/profile"

oauth = OAuth2Session(
    CLIENT_ID,
    redirect_uri='http://localhost:8000/login/token-code',
    auto_refresh_url=token_url,
    auto_refresh_kwargs={
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
)


def add_to_base_url(url, **kwargs):
    if kwargs:
        url += "?"

    for k, v in kwargs.items():
        url += f"{k}={v}&"

    return url.rstrip("&")


def ion_getcode_auth(request):
    if request.session.get('pk', None) is not None:
        return redirect(reverse('create-post'))

    auth_kwargs = {
        'client_id': CLIENT_ID,
        'response_type': 'code'
    }
    return redirect(add_to_base_url(authorize_url, **auth_kwargs))


def code_to_token(request):
    code = request.GET.get("code", None)
    if code is None:
        return render(
            request,
            'failed.html',
            {"description": "Did you prevent Ion access?"}
        )

    _ = oauth.fetch_token(
        token_url,
        code=code,
        client_secret=CLIENT_SECRET
    )
    profile = json.loads(
        oauth.get(profile_url).content.decode(encoding='utf-8')
    )
    blog_config = BlogConfig(  # type: ignore
        ion_username=profile['ion_username']
    )
    blog_config.save()
    request.session["pk"] = blog_config.id  # type: ignore

    return HttpResponseRedirect(reverse('create-post'))
