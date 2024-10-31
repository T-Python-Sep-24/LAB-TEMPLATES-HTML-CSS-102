from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse


def google_view(request:HttpRequest):
    return render(request,'main/index.html')

def tos_view(request:HttpRequest):
    return render(request,'main/tos.html')

def night_mode_view(request:HttpRequest):

    response=redirect('main:google_view')
    response.set_cookie('darkmode','dark',max_age=60*60*24)
    return response

def light_mode_view(request:HttpRequest):
    response=redirect('main:google_view')
    response.set_cookie('darkmode','dark',max_age=-3600)
    return response

    