from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # input book_id to find the item
    re_path(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
]
