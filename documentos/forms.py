
from django import forms
from django.forms import ModelForm
from .models import Documento

class DocumentoForm(ModelForm):

    class Meta:
        model = Documento
        fields = "__all__"

        widgets={
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "descripcion": forms.Textarea(attrs={'class':'form-control', 'rows':3, 'cols':50 }),
            "archivo" : forms.ClearableFileInput(attrs={"class":"form-control"}),
            "tipo": forms.Select(attrs={"class":"form-select"}),
            "estatus": forms.Select(attrs={"class":"form-select"}),
            "sistema": forms.Select(attrs={"class":"form-select"}),
        }

class ConsultaDocumentoForm(ModelForm):

    class Meta:
        model = Documento
        fields = ["nombre","descripcion","tipo","estatus","sistema"]

        widgets={
            "nombre": forms.TextInput(attrs={"class":"form-control", "disabled":True }),
            "descripcion": forms.Textarea(attrs={'class':'form-control', 'rows':3, 'cols':50 ,"disabled":True }),
            "tipo": forms.Select(attrs={"class":"form-select", "disabled":True}),
            "estatus": forms.Select(attrs={"class":"form-select", "disabled":True}),
            "sistema": forms.Select(attrs={"class":"form-select", "disabled":True}),
        }
