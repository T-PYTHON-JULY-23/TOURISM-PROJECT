
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("city/AlUla/", views.alula_view, name="alula_view"),
    path("city/Riyadh/", views.riyadh_view, name="riyadh_view"),
    path("city/Abha/", views.abha_view, name="abha_view"),
    path("city/Makkah/", views.makkah_view, name="makkah_view"),
    path("", views.home_view, name="home_view")



]