from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.display_view, name="display_view"),
    path('/city/makkah', views.makkah_view, name="makkah_view"),
    path('/city/abha', views.abha_view, name="abha_view"),
    path('/city/riyadh', views.riyadh_view, name="riyadh_view"),
    path('/city/alula', views.alula_view, name="alula_view"),
]