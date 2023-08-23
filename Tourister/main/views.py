from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def alula_view(request : HttpRequest):
    
    return render(request, "main/alula.html")

def makkah_view(request : HttpRequest):
    return render(request, "main/makkah.html")

def abha_view(request : HttpRequest):
    return render(request, "main/abha.html")

def riyadh_view(request : HttpRequest):
        return render(request, "main/riyadh.html")

def home_view(request : HttpRequest):
        return render(request, "main/home.html")