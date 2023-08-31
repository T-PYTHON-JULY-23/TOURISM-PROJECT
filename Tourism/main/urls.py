from django.urls import path 
from . import views

app_name ="main"

urlpatterns=[
    path("",views.view_sa,name="view_sa"),
    path("riyadh/",views.view_riyadh,name="view_riyadh"),
    path("jeddah/",views.view_jeddah,name="view_jeddah"),
    path("abha/",views.view_abha,name="view_abha"),
    path("makkah/",views.view_makkah,name="view_makkah"),
]