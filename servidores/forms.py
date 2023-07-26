
from django import forms
from django.forms import ModelForm
from .models import Servidor

class ServidorForm(ModelForm):

    class Meta:
        model = Servidor
        fields = "__all__"

        widgets={
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "ip" : forms.TextInput(attrs={"class":"form-control"}),
            "so": forms.Select(attrs={"class":"form-select"}),
            "tipo": forms.Select(attrs={"class":"form-select"}),
            "ambiente": forms.Select(attrs={"class":"form-select"}),
            "descripcion": forms.Textarea(attrs={'class':'form-control', 'rows':3, 'cols':50 }),
            "estatus": forms.Select(attrs={"class":"form-select"}),
        }


