from django.urls import path
from . import views

app_name='myapp'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('base/', views.base_view, name='base'),
    path('terms_of_service/', views.terms_of_service_view, name='terms_of_service'),
]