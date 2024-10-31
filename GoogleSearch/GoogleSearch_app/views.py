from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_page(request:HttpRequest):

    return render(request,"GoogleSearch_app/home_page.html")



def services_page(request:HttpRequest):

    return render(request,"GoogleSearch_app/services_page.html")






