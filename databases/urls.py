from django.contrib import admin
from django.urls import path

from . import views

app_name = 'databases'

urlpatterns = [
    path("", views.lista, name='lista'),
    path("agregar", views.DatabaseCreateView.as_view(),name='agregar'),
    path("ok", views.ok,name='ok'),
]

