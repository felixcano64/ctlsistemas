
from django import forms
from django.forms import ModelForm
from .models import Cambio

class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'

class CambioForm(ModelForm):

    class Meta:
        model = Cambio
        fields = "__all__"

        widgets={
            "numero": forms.TextInput(attrs={"class":"form-control"}),
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "tipo": forms.Select(attrs={"class":"form-select"}),
            "descripcion": forms.Textarea(attrs={'class':'form-control', 'rows':3, 'cols':50 }),
            "fechaInscripcion": DateTimeInput(),
            "fechaCambio": DateTimeInput(),
            "aplico": forms.TextInput(attrs={"class":"form-control"}),
            "resultado": forms.Select(attrs={"class":"form-select"}),
            "observacion": forms.Textarea(attrs={'class':'form-control', 'rows':3, 'cols':50 }),
            "componente": forms.Select(attrs={"class":"form-select"}),
            "smax": forms.Select(attrs={"class":"form-select"}),  
        }

