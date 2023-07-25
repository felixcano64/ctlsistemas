from django.contrib import admin
from django.urls import path

from . import views

app_name = 'sistemas'

urlpatterns = [
    path("", views.lista,name='lista'),
    path("agregar", views.SistemaCreateView.as_view(),name='agregar'),
    path("ok", views.ok,name='ok'),
]
