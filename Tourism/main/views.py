from django.shortcuts import render

from django.http import HttpResponse,HttpRequest

def home_view(request:HttpRequest):
    return render(request , "main/home.html")

def about_view(request: HttpRequest):

    return render(request, "main/about.html")
# Create your views here.
def abha_page(request:HttpRequest):

    return render(request,"main/abha.html")

def riyadh_page(request:HttpRequest):

    return render(request,"main/riyadh.html")

def makkah_page(request:HttpRequest):

    return render(request,"main/makkah.html")

def AlUla_page(request:HttpRequest):

    return render(request,"main/Alula.html")