from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.

class BlogViewPage(ListView):
    model = Post
    template_name = 'home.html'
