from django.contrib import admin
from django.urls import path

from . import views

app_name = 'documentos'

urlpatterns = [
    path("", views.DocumentoListView.as_view(), name='lista'),
    path("agregar", views.DocumentoCreateView.as_view(),name='agregar'),
    path("consulta/<int:pk>", views.DocumentoConsultaView.as_view(),name='consulta'),
    path("editar/<int:pk>", views.DocumentoUpdateView.as_view(),name='editar'),
    path("ok", views.ok,name='ok'),
]
