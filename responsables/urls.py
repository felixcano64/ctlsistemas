from django.contrib import admin
from django.urls import path

from . import views

app_name = 'responsables'

urlpatterns = [
    path("", views.ResponsableListView.as_view(), name='lista'),
    path("agregar", views.ResponsableCreateView.as_view(),name='agregar'),
    path("consulta/<int:pk>", views.ResponsableConsultaView.as_view(),name='consulta'),
    path("ok", views.ok,name='ok'),
]
