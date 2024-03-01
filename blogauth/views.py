from django.shortcuts import redirect, render
from secrets import CLIENT_ID, CLIENT_SECRET  # type: ignore


def add_to_base_url(url, **kwargs):
    if kwargs:
        url += "?"

    for k, v in kwargs.items():
        url += f"{k}={v}&"

    return url.rstrip("&")


def login_with_ion(_):
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
    url = ""
    return render(request, 'logged_in.html')
