# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    return HttpResponse("nihaozxx")


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")