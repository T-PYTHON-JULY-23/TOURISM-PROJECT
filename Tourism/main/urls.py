from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

    path('',views.home,name="home_page" ),
    path('city/Riyadh/',views.riyadh,name="riyadh_city" ),
    path('city/Abha/',views.abha,name="abha_city" ),
    path('city/Makkah/',views.makkah,name="makkah_city" ),
    path('city/AlUla/',views.alula,name="alula_city" ),
    path('city/jeddah/',views.jeddah,name="jeddah_city" )
]