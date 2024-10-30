from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def google(request: HttpRequest):
    return render(request, 'google.html')


def terms(request: HttpRequest):
    return render(request, 'terms.html')
