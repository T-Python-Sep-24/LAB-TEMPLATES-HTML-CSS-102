from django.urls import path
from . import views

app_name = 'google'
urlpatterns = [
    path('', views.home, name='home'),
    path('terms/', views.terms, name='terms'),
]