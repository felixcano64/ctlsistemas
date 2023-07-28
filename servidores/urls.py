from django.contrib import admin
from django.urls import path

from . import views

app_name = 'servidores'

urlpatterns = [
    path("", views.ServidorListView.as_view(), name='lista'),
    path("agregar", views.ServidorCreateView.as_view(),name='agregar'),
    path("consulta/<int:pk>", views.ServidorConsultaView.as_view(),name='consulta'),
    path("ok", views.ok,name='ok'),

]
