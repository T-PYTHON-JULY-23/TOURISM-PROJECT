from django.urls import path 
from . import views 

app_name= "main"

urlpatterns= [
    path ('', views.home_view , name= "home_view"),
    path('city/Riyadh/', views.Riyadh , name= "Riyadh"),
    path('city/Mekkah/', views.Mekkah , name= "Mekkah"),
    path('city/Abha/', views.Abha , name= "Abha"),
    path('city/AlUla/', views.AlUla , name= "AlUla")
]