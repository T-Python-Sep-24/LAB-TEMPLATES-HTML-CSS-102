from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.main, name='main'),
    path('terms/', views.terms, name='terms'),
]
