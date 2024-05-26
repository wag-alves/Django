from django.urls import path
from recipes.views import contato, home, my_view

urlpatterns = [
    path('sobre/', my_view),
    path("", home),
    path("contato/", contato),
]
