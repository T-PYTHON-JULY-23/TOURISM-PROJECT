from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("city/Riyadh/", views.riyadh_view, name="riyadh_view"),
    path("city/Abha/", views.abha_view, name="abha_view"),
    path("city/Jeddah/", views.jeddah_view, name="jeddah_view"),
    path("city/Mekkah/", views.mekkah_view, name="mekkah_view"),
]