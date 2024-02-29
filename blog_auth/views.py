from django.views.generic import TemplateView
from config import Config


class AuthPage(TemplateView):
    template_name = "auth.html"


class BlogView(TemplateView):
    @property
    def template_name(self) -> str:
        if Config().authorized:
            return "blog.html"
        return "404.html"
