from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def home_view(request):
    return render(request,'main/home.html')


def riyadh_view(request):
    return render(request,'main/riyadh.html')

def makkah_view(request):
    
    return render(request,'main/Mekkah.html')
def abha_view(request):
    
    return render(request,'main/abha.html')
def alula_view(request):
    
    return render(request,'main/alula.html')