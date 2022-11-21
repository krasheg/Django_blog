from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'title': 'Main page'})


def about(request):
    return render(request, 'women/about.html', {'title': "About"})


def categories(request, cat_id):
    return HttpResponse(f'Categories for {cat_id=}')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
