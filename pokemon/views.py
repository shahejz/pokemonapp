from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'base.html', {'html_var': 'index'})

def index1(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'base.html', {'html_var': 'index1'})

def index2(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'base.html', {'html_var': 'index2'})