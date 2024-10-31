from . import views
from django.urls import path 

app_name = "GoogleSearch_app"

urlpatterns = [
   path("", views.home_page, name="home_page"),
   path("terms/", views.services_page, name="services_page"),
]


