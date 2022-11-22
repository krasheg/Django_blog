from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add post', 'url_name': 'add_page'},
        {'title': 'Contacts', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'},
        ]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': "Main page"
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


def show_post(request, post_id):
    obj = Women.objects.filter(id=post_id).first()
    text = obj.content
    return HttpResponse(f"{text}")

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
