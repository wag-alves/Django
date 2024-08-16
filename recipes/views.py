# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "recipes/pages/home.html", context={
        'nome': 'Wagner',
    })


def recipe(request, id):
    return render(request, "recipes/pages/recipe-view.html", context={
        'nome': 'Wagner',
    })

# Create your views here.
# def my_view(request):
#     return HttpResponse("QUE STRING LINDA")

# def contato(request):
#     return HttpResponse("Você está na pagina de contato!")
