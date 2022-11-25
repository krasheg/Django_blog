from django import template
from women.models import *

register = template.Library()


@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    return Category.objects.filter(pk=filter)


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats,'cat_selected': cat_selected}


@register.inclusion_tag('women/menu.html')
def main_menu():

    menu = [{'title': 'About', 'url_name': 'about'},
            {'title': 'Add post', 'url_name': 'add_page'},
            {'title': 'Contacts', 'url_name': 'contact'},
            {'title': 'Login', 'url_name': 'login'},
            ]
    return {'menu': menu}


@register.inclusion_tag('women/list_posts.html')
def show_posts(cat_selected=0):
    if cat_selected:
        posts = Women.objects.filter(cat__slug=cat_selected)
    else:
        posts = Women.objects.all()
    return {'posts': posts}
