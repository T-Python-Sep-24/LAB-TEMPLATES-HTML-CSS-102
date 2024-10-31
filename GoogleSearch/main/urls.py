from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),  
    path('terms/', views.term_view, name='term_view'),
    
]
