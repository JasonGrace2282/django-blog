from django.http import HttpResponse

# Create your views here.

def home_page_view(request) -> HttpResponse:
    return HttpResponse("Hello, World!")
