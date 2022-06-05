from django.shortcuts import render


def home(request):
    return render(request, 'general/home.html')


def about(request):
    return render(request, 'general/about.html', {'title': 'About'})
