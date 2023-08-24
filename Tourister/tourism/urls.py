from django.urls import path
from . import views

app_name = "Tourister"

urlpatterns = [
    path('', views.home, name="home_view"),
    path('city/Riyadh/', views.riyadh, name="riyadh_view"),
    path('city/Abha/', views.Abha, name="Abha_view"),
    path('city/Mekkah/', views.Mekkah, name="Mekkah_view"),
    path('city/Alula/', views.Alula, name="Alula_viwe"),
    path('city/', views.City, name="City"),
    path('VideoR/', views.ryidF, name="RCity"),
    path('VideoA/', views.AbhaV, name="Abhav"),
    path('VideoAl/', views.AlulaV, name="ACity"),
    path('VideoRM/', views.MekkahV, name="MCity")


]