from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('blogs/', views.blog_view, name="blog_view"),
    path('about/', views.about_view, name="about_view"),
    path('discover/', views.discover_view, name="discover_view"),
    path('hail/', views.hail_view, name="hail_view"),
    path('qassim/', views.qassim_view, name="qassim_view"),
    path('umluj/', views.umluj_view, name="umluj_view"),
    path('fursan/', views.fursan_view, name="fursan_view"),


    
    
]