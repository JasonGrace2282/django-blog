from __future__ import annotations

from requests_oauthlib import OAuth2Session
from secret import CLIENT_ID,  CLIENT_SECRET

__all__ = ["BlogConfig"]


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton,
                cls
            ).__call__(*args, **kwargs)
        return cls._instances[cls]


authorize_url = "https://ion.tjhsst.edu/oauth/authorize/"
token_url = "https://ion.tjhsst.edu/oauth/token/"


class _BlogConfig(metaclass=Singleton):
    ion_oauthed = False
    oauth = OAuth2Session(
        CLIENT_ID,
        redirect_uri='http://localhost:8000/login/token-code',
        auto_refresh_url=token_url,
        auto_refresh_kwargs={
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
    )


BlogConfig = _BlogConfig()
