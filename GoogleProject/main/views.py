from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def main_view(request:HttpRequest):

    return render(request, "main/google.html")



def term_view(request:HttpRequest):

    return render(request, "main/term.html")
