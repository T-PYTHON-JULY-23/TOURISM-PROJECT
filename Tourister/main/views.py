from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_view(request : HttpRequest):

    return render(request, "main/home.html",)

def riyadh_view(request : HttpRequest):

    return render(request, "main/riyadh.html",)

def abha_view(request : HttpRequest):

    return render(request, "main/abha.html",)

def jeddah_view(request : HttpRequest):

    return render(request, "main/jeddah.html",)
def mekkah_view(request : HttpRequest):

    return render(request, "main/mekkah.html",)