from django.shortcuts import render
from django.http import HttpResponse , HttpRequest

# Create your views here.

def view_sa (request):

    return render(request , 'main/saudi_arabia.html')

def view_riyadh(request):
    
    return render(request,'main/riyadh.html')

def view_jeddah (request):

    return render(request,'main/jeddah.html')

def view_abha(request):

    return render(request ,'main/abha.html')

def view_makkah(request ):

    return render(request, 'main/makkah.html')
