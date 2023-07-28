from django.contrib import admin
from django.urls import path

from . import views

app_name = 'componentes'

urlpatterns = [
    path("", views.ComponenteListView.as_view(), name='lista'),
    path("agregar", views.ComponenteCreateView.as_view(),name='agregar'),
    path("consulta/<int:pk>", views.ComponenteConsultaView.as_view(),name='consulta'),
    path("ok", views.ok,name='ok'),
]
