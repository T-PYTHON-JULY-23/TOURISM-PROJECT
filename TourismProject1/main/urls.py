from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path('about/', views.about_view, name="about_view"),
    path('riyadh/', views.riyadh_view, name="riyadh_view"),
    path('alula/', views.alula_view, name="alula_view"),
    path('jeddah/', views.jeddah_view, name="jeddah_view"),
    path('abha/', views.abha_view, name="abha_view")
    
    
]