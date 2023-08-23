from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.home_view,name='home_view'),
    path('city/Riyadh/', views.riyadh_view,name='riyadh_view'),
    path('city/Mekkah/', views.makkah_view,name='Mekkah_view'),
    path('city/Abha/', views.abha_view ,name='abha_view'),
    path('city/AlUla/', views.alula_view ,name='alula_view'),
]