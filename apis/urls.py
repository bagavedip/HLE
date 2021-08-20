from .views import convert
from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('convert/', views.convert, name='convert'),
#    path('', views.abc, name="abc"),
]
