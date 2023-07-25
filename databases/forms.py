
from django import forms
from django.forms import ModelForm
from .models import Database

class DatabaseForm(ModelForm):

    class Meta:
        model = Database
        fields = "__all__"

        widgets={
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "manejador": forms.TextInput(attrs={"class":"form-control"}),
            "usuario": forms.TextInput(attrs={"class":"form-control"}),
            "password": forms.TextInput(attrs={"class":"form-control"}),
            "puerto": forms.TextInput(attrs={"class":"form-control"}),
            "servidor": forms.Select(attrs={"class":"form-select"}),
        }

