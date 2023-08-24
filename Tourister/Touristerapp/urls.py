from django.urls import path
from Touristerapp import views

app_name = "Touristerapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('jeddah/', views.jeddah, name='jeddah'),
    path('riyadh/', views.riyadh, name='riyadh'),
    path('alula/', views.alula, name='alula'),
    path('neom/', views.neom, name='neom'),
]
