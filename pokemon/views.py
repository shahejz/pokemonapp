from django.http import HttpResponse
from django.shortcuts import render

from .models import Pokemon

def index(request):
    queryset = Pokemon.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, "index.html", context)

def pokemon(request, name):
    queryset = Pokemon.objects.get(name=name)
    context = {
        "obj": queryset
    }

    return render(request, "pokemon.html", context)