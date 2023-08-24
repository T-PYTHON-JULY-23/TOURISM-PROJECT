from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home_view(request:HttpRequest):
    return render(request, "main/index.html")


def about_view(request:HttpRequest):
    return render(request, "main/about.html")

def riyadh_view(request: HttpRequest):

    return render(request, "main/riyadh.html")


def alula_view(request: HttpRequest):

    return render(request, "main/alula.html")



def abha_view(request: HttpRequest):

    return render(request, "main/abha.html")

def jeddah_view(request: HttpRequest):

    return render(request, "main/jeddah.html")