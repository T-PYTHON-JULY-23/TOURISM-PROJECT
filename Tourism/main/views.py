from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.


def home(request : HttpRequest):
    
    return render(request, "main/home.html")

def riyadh(request : HttpRequest):
    
    return render(request, "main/riyadh.html")
def abha(request : HttpRequest):
    
    return render(request, "main/abha.html")
def makkah(request : HttpRequest):
    
    return render(request, "main/makkah.html")
def alula(request : HttpRequest):
    
    return render(request, "main/alula.html")
def jeddah(request : HttpRequest):
    
    return render(request, "main/jeddah.html")
