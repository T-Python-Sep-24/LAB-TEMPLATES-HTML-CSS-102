from django.shortcuts import render


def main(request):
    return render(request, 'main/main.html')

def terms(request):
    return render(request, 'main/terms.html')
