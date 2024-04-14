from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html", context={
        'nome': 'Wagner',
    })


def contato(request):
    return HttpResponse("Você está na pagina de contato!")
