from django.shortcuts import render
from django.http import HttpRequest

#Home page
def mainView(request: HttpRequest):
    return render(request, "main/mainPage.html")

#Terms page
def termsView(request: HttpRequest):
    return render(request, "main/termsPage.html")