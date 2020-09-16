from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.


def Home(request):
    return HttpResponse("<h1> This is home page </h1>")


def News(request):
    return HttpResponse("<h1> This is news page </h1>")


def Contact(request):
    return HttpResponse("<h1> This is contact page </h1>")


