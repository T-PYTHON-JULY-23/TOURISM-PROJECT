from django.shortcuts import render
from django.http import HttpRequest , HttpResponse


def home_page(request : HttpRequest):

    return render(request, "main/homePage.html")
# Create your views here.

def eastern_viwe(request : HttpRequest):

    return render(request, "main/eastern.html")

def dammam_viwe(request : HttpRequest):

    return render(request, "main/dammam.html")


def hasa_viwe(request : HttpRequest):

    return render(request, "main/hasa.html")


def habar_viwe(request : HttpRequest):

    return render(request, "main/alkhabr.html")

def riyadh_viwe(request : HttpRequest):

    return render(request, "main/riyadh.html")

def southHren_viwe(request : HttpRequest):

    return render(request, "main/southHren.html")


def jeddah_viwe(request : HttpRequest):

    return render(request, "main/jeddah.html")

def makkah_viwe(request : HttpRequest):

    return render(request, "main/makkah.html")

def medina_viwe(request : HttpRequest):

    return render(request, "main/medina.html")

