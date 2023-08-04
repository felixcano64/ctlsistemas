from django.contrib import admin
from django.urls import path

from . import views

app_name = 'sistemas'

urlpatterns = [
    path("", views.SistemaListView.as_view(),name='lista'),
    path("agregar", views.SistemaCreateView.as_view(),name='agregar'),
    path("consulta/<int:pk>", views.SistemaConsultaView.as_view(),name='consulta'),
    path("editar/<int:pk>", views.SistemaUpdateView.as_view(),name='editar'),
    path("ok", views.ok,name='ok'),
]
