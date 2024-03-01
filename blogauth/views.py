from django.shortcuts import redirect, render
from secrets import CLIENT_ID, CLIENT_SECRET  # type: ignore


def login_with_ion(_):
    kwargs = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "response_type": "code"
    }
    url = "https://ion.tjhsst.edu/oauth/authorize/"
    if kwargs:
        url += "?"

    for k, v in kwargs.items():
        url += f"{k}={v}&"

    return redirect(url.rstrip("&"))


def auth_code(request):
    code = request.GET.get("code", None)
    if code is None:
        return render(
            request,
            'failed.html',
            {"description": "Did you prevent Ion access?"}
        )
    print(code)
    return render(request, 'logged_in.html')
