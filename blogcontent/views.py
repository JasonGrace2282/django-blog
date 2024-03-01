from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from config import BlogConfig


class BlogView(TemplateView):
    template_name = "blog.html"

    @property
    def context(self) -> dict[str, str]:
        return BlogConfig.header


def create_view(request):
    if BlogConfig.admin_data is None:
        return redirect('/admin')
    return render(request, 'create.html')
