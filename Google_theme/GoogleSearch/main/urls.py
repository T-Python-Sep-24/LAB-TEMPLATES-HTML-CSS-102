from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

    path("",views.home_view , name = "home_view"),
    path("base/",views.base_view , name = "base_view"),
    path("terms/",views.terms_view , name = "terms_view"),

]