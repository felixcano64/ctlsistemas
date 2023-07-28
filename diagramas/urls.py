from django.contrib import admin
from django.urls import path

from . import views

app_name = 'diagramas'

urlpatterns = [
    path("", views.DiagramaListView.as_view(), name='lista'),
    path("agregar", views.DiagramaCreateView.as_view(),name='agregar'),
    path("consulta/<int:pk>", views.DiagramaConsultaView.as_view(),name='consulta'),
    path("ok", views.ok,name='ok'),

]
