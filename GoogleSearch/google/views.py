from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def search_view(request: HttpRequest):
    return render(request, "google/search.html")

def terms_view(request: HttpRequest):
    return render(request, "google/terms.html")

