from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_view, name="main_view"),
    path("google/", views.main_view, name="google"),
    path("erms and services/", views.term_view, name="term"),


]