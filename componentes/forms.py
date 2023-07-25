
from django import forms
from django.forms import ModelForm
from .models import Componente

class ComponenteForm(ModelForm):

    class Meta:
        model = Componente
        fields = "__all__"

        widgets={
            "nombreCorto": forms.TextInput(attrs={"class":"form-control"}),
            "nombreLargo": forms.TextInput(attrs={"class":"form-control"}),
            "descripcion": forms.Textarea(attrs={'class':'form-control', 'rows':3, 'cols':50 }),
            "version": forms.TextInput(attrs={"class":"form-control"}),
            "tipo": forms.Select(attrs={"class":"form-select"}),
            "estatus": forms.Select(attrs={"class":"form-select"}),
            "sistema": forms.Select(attrs={"class":"form-select"}),
            "servidor": forms.Select(attrs={"class":"form-select"}),  
            "database": forms.Select(attrs={"class":"form-select"}),   
        }

