from django.urls import path
from . import views

app_name = 'main'

urlpatterns=[
    path('',views.home, name="home_view"),
    path('tourism_saudi/', views.tourism , name="tourismsaudi_view"),
    path('regons/', views.regons, name='regons_view'),
    path('city/Riyadh/', views.riyadh, name='riyadh_view'),
    path('city/jeddah/', views.jeddah, name='jeddah_view'),
    path('city/alkhobar/', views.jeddah, name='alkhobar_view'),
    path('city/umluj/', views.jeddah, name='umluj_view'),
]