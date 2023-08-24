from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("" , views.home_view,name="home_view"),
    path('city/about/', views.about_view, name="about_view"),
   path('city/Abha/', views.abha_page, name="abha_page"),
    path('city/Riyadh/', views.riyadh_page, name="riyadh_page"),
    path('city/makkah/', views.makkah_page, name="makkah_page"),
    path('city/Alula/', views.AlUla_page, name="AlUla_page"),

]