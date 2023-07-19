from django.shortcuts import render
from django.http import HttpResponse


def homeView(request):
    """A function to access the home view"""
    return HttpResponse("<h1>Welcome to All You can Eat!</h1>")
    