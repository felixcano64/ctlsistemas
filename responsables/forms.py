
from django import forms
from django.forms import ModelForm
from .models import Responsable

class ResponsableForm(ModelForm):

    class Meta:
        model = Responsable
        fields = "__all__"

        widgets={
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "apPaterno": forms.TextInput(attrs={"class":"form-control"}),
            "apMaterno": forms.TextInput(attrs={"class":"form-control"}),
            "area": forms.TextInput(attrs={"class":"form-control"}),
            "puesto": forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.TextInput(attrs={"class":"form-control"}),
            "telefono": forms.TextInput(attrs={"class":"form-control"}),
        }

