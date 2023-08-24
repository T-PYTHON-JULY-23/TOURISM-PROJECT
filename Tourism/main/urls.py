from django.urls import path
from . import views


app_name = "main"

urlpatterns = [

    path('', views.home_page , name="home_page"),
    path('eastern/', views.eastern_viwe, name="eastern_viwe"),
    path('eastern/dammam/', views.dammam_viwe, name="dammam_viwe"),
    path('eastern/hasa/', views.hasa_viwe, name="hasa_viwe"),
    path('eastern/khabar/', views.habar_viwe, name="habar_viwe"),
    path('riyadh/', views.riyadh_viwe, name="riyadh_viwe"),
    path('southren_viwe/', views.southHren_viwe, name="southHren_viwe"),
    path('southren/jeddah', views.jeddah_viwe, name="jeddah_viwe"),
    path('southren/makkah', views.makkah_viwe, name="makkah_viwe"),
    path('southren/medina', views.medina_viwe, name="medina_viwe"),
    
]
