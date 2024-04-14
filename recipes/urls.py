
from django.http import HttpResponse
from django.urls import path
from recipes.views import contato, home


def my_view(request):
    return HttpResponse("QUE STRING LINDA")


urlpatterns = [
    path('sobre/', my_view),
    path("", home),
    path("contato/", contato),
]
