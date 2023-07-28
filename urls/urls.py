from django.contrib import admin
from django.urls import path

from . import views

app_name = 'urls'

urlpatterns = [
    path("", views.UrlListView.as_view(),name='lista'),
    path("agregar", views.UrlCreateView.as_view(),name='agregar'),
    path("consulta/<int:pk>", views.UrlConsultaView.as_view(),name='consulta'),
    path("ok", views.ok,name='ok'),

]
