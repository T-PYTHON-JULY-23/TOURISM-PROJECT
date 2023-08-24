from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def riyadh(request):
    return render(request, 'pages/Riyadh.html')

def Abha(request):
    return render(request, 'pages/Abha.html')

def Mekkah(request):
    return render(request, 'pages/Mekkah.html')

def Alula(request):
    return render(request, 'pages/Alula.html')

def City(request):
    return render(request, 'pages/City.html')

def ryidF(request):
    return render(request, 'pages/riydF.html')

def AbhaV(request):
    return render(request, 'pages/AbhaV.html')

def AlulaV(request):
    return render(request, 'pages/Alulav.html')

def MekkahV(request):
    return render(request, 'pages/Makkahv.html')