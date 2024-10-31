from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest , HttpResponse 


def home_view(request:HttpRequest):
    
    return render(request , "main/home.html")

def service_view(request:HttpRequest):

    return render(request , "main/service.html")