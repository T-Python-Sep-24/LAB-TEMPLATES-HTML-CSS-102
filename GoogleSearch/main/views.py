from django.shortcuts import render

from django.shortcuts import render

def index_view(request):
    return render(request, 'main/index.html')

def terms_view(request):
    return render(request, 'main/terms.html') # Create your views here.
