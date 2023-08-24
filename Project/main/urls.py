from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('',views.home_view, name = "home_view"),
    path('riyadh/',views.riyadh_view, name = "riyadh_view"),
    path('riyadh2/',views.riyadh2_view, name = "riyadh2_view"),
    path('hail/',views.hail_view, name= "hail_view"),
    path('hail2/', views.hail2_view, name = "hail2_view"),
    path('Ula/',views.Ula_view, name= "Ula_view"),
    path('Ula2/',views.Ula2_view, name= "Ula2_view"),
    path('khobar/',views.khobar_view, name= "khobar_view"),
    path('khobar2/',views.khobar2_view, name="Khobar2_view"),

]