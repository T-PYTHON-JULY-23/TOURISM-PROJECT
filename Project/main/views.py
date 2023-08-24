from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def home_view(request : HttpRequest) :

    return render(request, "main/home.html")

def riyadh_view(request : HttpRequest):

    return render(request, "main/riyadh.html")

def riyadh2_view(request : HttpRequest):

    return render(request,"main/riyadh2.html")

def hail_view(request : HttpRequest):

    return render(request,"main/hail.html")

def hail2_view(request : HttpRequest):
 
    return render(request,"main/hail2.html")

def Ula_view(request : HttpRequest):

    return render(request,"main/Ula.html")

def Ula2_view(request : HttpRequest):

    return render(request,"main/Ula2.html")

def khobar_view(request: HttpRequest):

    return render(request,"main/khobar.html")

def khobar2_view(request: HttpRequest):

    return render(request,"main/khobar2.html")