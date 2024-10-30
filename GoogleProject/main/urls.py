from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.google_view, name="google"),
    path("google/", views.google_view, name="google"),
    path("erms and services/", views.term_view, name="term"),


]