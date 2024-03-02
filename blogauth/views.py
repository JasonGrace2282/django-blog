from django.shortcuts import redirect, render
from config import BlogConfig, authorize_url, CLIENT_ID
from django.http.response import HttpResponseRedirect


def add_to_base_url(url, **kwargs):
    if kwargs:
        url += "?"

    for k, v in kwargs.items():
        url += f"{k}={v}&"

    return url.rstrip("&")


def ion_getcode_auth(request):
    if BlogConfig.ion_oauthed:
        return redirect('/admin/')

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
    BlogConfig.ion_oauthed = True
    return HttpResponseRedirect('/admin/')
