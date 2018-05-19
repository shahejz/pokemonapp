from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Pokemon

def index(request):
    queryset = Pokemon.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 50)
    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)

    context = {
        "object_list": p
    }

    return render(request, "index.html", context)

def pokemon(request, name=None, number=None):
    if name:
        queryset = Pokemon.objects.get(name=name)
    else:
        queryset = Pokemon.objects.get(number=int(number))

    context = {
        "obj": queryset
    }

    return render(request, "pokemon.html", context)

def gen(request, gen=1):
    queryset = Pokemon.objects.filter(gen=gen)
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 50)
    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)

    context = {
        "object_list": p
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

    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 50)
    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)

    context = {
        "object_list": p
    }

    return render(request, "index.html", context)