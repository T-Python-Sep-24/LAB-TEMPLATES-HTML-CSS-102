from django.urls import path
from . import views

app_name = "google"

urlpatterns = [
    path("", views.search_view, name="search_view"),
    path("terms/", views.terms_view, name="terms_view")
]