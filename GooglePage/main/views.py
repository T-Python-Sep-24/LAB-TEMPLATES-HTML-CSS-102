from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.

def home_view(request):
    return render(request,"main/home_page.html")

def terms_view(request):
    return render(request,"main/terms_page.html")
