from django.contrib import admin
from django.urls import path

from . import views

app_name = 'responsables'

urlpatterns = [
    path("", views.lista, name='lista')
]
