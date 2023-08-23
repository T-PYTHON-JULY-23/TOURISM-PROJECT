from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request : HttpRequest):

    #to read a cookie
    #mode = request.COOKIES.get("mode", "light")

    return render(request, "main/home.html")


def makkah_view(request: HttpRequest):

    return render(request, "main/city/makkah.html")

def riyadh_view(request: HttpRequest):

    return render(request, "main/city/riyadh.html")

def alhassa_view(request: HttpRequest):

    return render(request, "main/city/alhassa.html")

def dammam_view(request: HttpRequest):

    return render(request, "main/city/dammam.html")