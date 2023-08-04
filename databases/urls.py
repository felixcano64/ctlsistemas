from django.contrib import admin
from django.urls import path

from . import views

app_name = 'databases'

urlpatterns = [
    path("", views.DatabaseListView.as_view(), name='lista'),
    path("agregar", views.DatabaseCreateView.as_view(),name='agregar'),
    path("consulta/<int:pk>", views.DatabaseConsultaView.as_view(),name='consulta'),
    path("editar/<int:pk>", views.DatabaseUpdateView.as_view(),name='editar'),
    path("ok", views.ok,name='ok'),
]

