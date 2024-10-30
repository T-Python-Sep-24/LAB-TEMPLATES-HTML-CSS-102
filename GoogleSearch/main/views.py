from django.shortcuts import render
from django.http import HttpRequest


def google_view(request:HttpRequest):
    return render(request,'main/index.html')

def tos_view(request:HttpRequest):
    return render(request,'main/tos.html')