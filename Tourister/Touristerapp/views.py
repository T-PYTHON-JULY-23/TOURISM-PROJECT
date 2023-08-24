from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home(request:HttpRequest):
    return render(request, 'Touristerapp/home.html')

def jeddah(request:HttpRequest):
    return render(request, 'Touristerapp/jeddah.html')

def riyadh(request:HttpRequest):
    return render(request, 'Touristerapp/riyadh.html')

def alula(request:HttpRequest):
    return render(request, 'Touristerapp/alula.html')

def neom(request:HttpRequest):
    return render(request, 'Touristerapp/neom.html')
