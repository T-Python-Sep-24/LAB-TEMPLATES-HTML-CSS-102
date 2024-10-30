from django.urls import path

from . import views
app_name = 'cloneGoogleApp'
urlpatterns = [
    path("", views.google, name="google_view"),
    path("terms/", views.terms, name="terms_view")

]