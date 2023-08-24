from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home(request:HttpRequest):
    return render(request,'main/home.html')
def tourism (request:HttpRequest):
    return render(request,'main/tourism_saudi.html')

def regons(request:HttpRequest):
    return render(request, 'main/regons.html')

def riyadh(request:HttpRequest):
    return render(request, 'main/riyadh.html')

def jeddah(request:HttpRequest):
    return render(request, 'main/jeddah.html')

def alkhobar(request:HttpRequest):
    return render(request, 'main/alkhobar.html')

def umluj(request:HttpRequest):
    return render(request, 'main/umluj.html')

