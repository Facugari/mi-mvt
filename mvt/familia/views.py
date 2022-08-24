from django.shortcuts import render
from .models import Familiares


def home (request):
    return render (request, 'home.html', context={} )

def flia(request):
    flia = Familiares(nombre ="facundo", edad=25, fecha= "1996-10-04")
    flia.save()
    context = {'flia': flia}
    return render (request, 'home.html', context)

def hno(request):
    hno = Familiares(nombre ="lucas", edad=32, fecha= "1991-10-23")
    hno.save()
    context = {'hno': hno}
    return render (request, 'home.html', context)

def primo(request):
    primo = Familiares(nombre ="Esteban", edad=10, fecha= "1912-10-23")
    primo.save()
    context = {'primo': primo}
    return render (request, 'home.html', context)