from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

# Create your views here.

def home_view(request :HttpRequest):
    return render (request , "main/home.html")

def Riyadh( request : HttpRequest):
    return render (request , "main/Riyadh.html")

def Mekkah( request : HttpRequest):
    return render (request , "main/Mekkah.html")

def Abha( request : HttpRequest):
    return render (request , "main/Abha.html")

def AlUla( request : HttpRequest):
    return render (request , "main/AlUla.html")