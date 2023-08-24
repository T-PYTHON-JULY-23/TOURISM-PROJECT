from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request:HttpRequest) -> HttpResponse:
    return render(request, 'main/home.html')

def riyadh_view(request:HttpRequest) -> HttpResponse:
    return render(request, 'main/riyadh.html')

def makkah_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/makkah.html')
def baha_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/baha.html')
def dammam_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/dammam.html')