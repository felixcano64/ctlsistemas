from django.contrib import admin
from django.urls import path

from . import views

app_name = 'cambios'

urlpatterns = [
    path("", views.CambioListView.as_view(),name='lista'),
    path("agregar", views.CambioCreateView.as_view(),name='agregar'),
    path("consulta/<int:pk>", views.CambioConsultaView.as_view(),name='consulta'),
    path("ok", views.ok,name='ok'),
]
