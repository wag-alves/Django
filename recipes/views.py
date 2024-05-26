from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def my_view(request):
    return HttpResponse("QUE STRING LINDA")


def home(request):
    return render(request, "home.html", context={
        'nome': 'Wagner',
    })


def contato(request):
    return HttpResponse("Você está na pagina de contato!")
