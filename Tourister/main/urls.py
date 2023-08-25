from django.urls import path
from . import views


app_name="main"

urlpatterns=[

    path('',views.home_view,name="home_view"),
    path('city/riyadh/',views.riyadh_view,name="riyadh_view"),
    path('city/makkah/',views.makkah_view,name="makkah_view"),
    path('city/abha/',views.abha_view,name="abha_view"),
    path('city/AlKhobar/',views.AlKhobar_view,name="AlKhobar_view"),
]

