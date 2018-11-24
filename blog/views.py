from django.shortcuts import render, redirect
from . import views
from django.views.generic import CreateView, TemplateView
from django.utils import timezone
from .models import Post
# Create your views here.
def post_list(request):
    return render(request, 'blog/index.html', {})

def galeria(request):
    return render(request, 'blog/galeria.html', {})    