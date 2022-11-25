from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


# Create your views here.


def index(request):
    context = {
        'title': "Main page",
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': "About"})


def addpage(request):
    return HttpResponse('Adding a new post')


def contact(request):
    return HttpResponse('Contact us')


def login(request):
    return HttpResponse('Authorization')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request,'women/post.html', context=context)


def show_category(request, cat_slug):
    context = {
        'title': "Categories",
        'cat_selected': cat_slug,
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
