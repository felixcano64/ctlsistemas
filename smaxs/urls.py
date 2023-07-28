from django.contrib import admin
from django.urls import path

from . import views

app_name = 'smaxs'

urlpatterns = [
    path("", views.SmaxListView.as_view(),name='lista'),
    path("agregar", views.SmaxCreateView.as_view(),name='agregar'),
    path("consulta/<int:pk>", views.SmaxConsultaView.as_view(),name='consulta'),
    path("ok", views.ok,name='ok'),

]
