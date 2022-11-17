from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse('Application page')


def categories(request, cat_id):
    return HttpResponse(f'Categories for {cat_id=}')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
