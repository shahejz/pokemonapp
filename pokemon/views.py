from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

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

def gen(request, gen=1):
    queryset = Pokemon.objects.filter(gen=gen)
    context = {
        "object_list": queryset
    }

    return render(request, "index.html", context)

def type(request, type=None):
    if type == None:
        queryset = Pokemon.objects.order_by("type1").values("type1").distinct()
        context = {
            "types": queryset
        }

        return render(request, "types.html", context)

    queryset = Pokemon.objects.filter(Q(type1=type) | Q(type2=type))
    context = {
        "object_list": queryset
    }

    return render(request, "index.html", context)