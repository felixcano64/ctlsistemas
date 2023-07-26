
from django import forms
from django.forms import ModelForm
from .models import Diagrama

class DiagramaForm(ModelForm):

    class Meta:
        model = Diagrama
        fields = "__all__"

        widgets={
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "descripcion": forms.Textarea(attrs={'class':'form-control', 'rows':3, 'cols':50 }),
            "path": forms.TextInput(attrs={"class":"form-control"}),
            "tipo": forms.Select(attrs={"class":"form-select"}),
            "estatus": forms.Select(attrs={"class":"form-select"}),
            "sistema": forms.Select(attrs={"class":"form-select"}),
        }

