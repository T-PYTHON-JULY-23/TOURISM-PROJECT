from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home_view(request):

    return render(request,'main/home_view.html')

def riyadh_view(request):
    
    return render(request,'main/riyadh_view.html')

def abha_view(request):
    
    return render(request,'main/abha_view.html')

def mekkah_view(request):
    
    return render(request,'main/mekkah_view.html')

def alula_view(request):
    
    return render(request,'main/alula_view.html')
