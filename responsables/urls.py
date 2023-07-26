from django.contrib import admin
from django.urls import path

from . import views

app_name = 'responsables'

urlpatterns = [
    path("", views.lista, name='lista'),
    path("agregar", views.ResponsableCreateView.as_view(),name='agregar'),
    path("ok", views.ok,name='ok'),
]
