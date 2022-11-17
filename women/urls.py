from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('categories/<int:cat_id>/', views.categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive),
]
