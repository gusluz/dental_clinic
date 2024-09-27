from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    return render(request, 'landpage/index.html')


def teste(request):
    return render(request, 'base.html')

def teste404(request):
    return render(request, '404.html')
