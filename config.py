from django.views.generic import TemplateView


__all__ = [
    "Config",
    "config"
]


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton,
                cls
            ).__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=Singleton):
    authorized: bool = False


config = Config()


class RenderIfLoggedIn(TemplateView):
    main: str
    backup: str = "404.html"

    @property
    def template_name(self) -> str:
        return self.main if config.authorized else self.backup
