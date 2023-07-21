from django.contrib import admin
from django.urls import path

from . import views

app_name = 'servidores'

urlpatterns = [
    path("", views.lista, name='lista'),
]
