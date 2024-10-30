from django.shortcuts import render


def home_view(request):
    return render(request, 'myapp/home.html')

def base_view(request):
    return render(request, 'myapp/base.html')

def terms_of_service_view(request):
    return render(request, 'myapp/terms_of_service.html')