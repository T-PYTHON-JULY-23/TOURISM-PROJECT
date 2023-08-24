from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest

# Create your views here.
def main_view(request:HttpRequest):
    return render(request,'main/base.html')

def home_view(request : HttpRequest):

    return render(request, "main/home.html")

def blog_view(request : HttpRequest):
    return render(request, "main/maintenance.html")

def about_view(request : HttpRequest):
    return render(request, "main/maintenance.html")
def hail_view(request : HttpRequest):
    return render(request, "main/hail.html")
def fursan_view(request : HttpRequest):
    return render(request, "main/maintenance.html")
def qassim_view(request : HttpRequest):
    return render(request, "main/maintenance.html")
def umluj_view(request : HttpRequest):
    return render(request, "main/maintenance.html")



