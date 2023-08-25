from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.

def home_view (request:HttpRequest):

    return render(request,"main/index.html")

def riyadh_view (request:HttpRequest):
    return render(request,"main/Riyadh.html")

def makkah_view (request:HttpRequest):
    return render(request,"main/makkah.html")

def abha_view (request:HttpRequest):
    return render(request,"main/abha.html")

def AlKhobar_view (request:HttpRequest):
    return render(request,"main/AlKhobar.html")