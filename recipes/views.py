from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "recipes/home.html", context={
        'name': "Luccas",
    })

def sobre(request):
    return render(request, 'me-apague/temp.html')

def contato(request):
    return HttpResponse("CONTATO")