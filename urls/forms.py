
from django import forms
from django.forms import ModelForm
from .models import Url

class UrlForm(ModelForm):

    class Meta:
        model = Url
        fields = "__all__"

        widgets={
            "urlInterna":forms.TextInput(attrs={"class":"form-control"}),
            "urlExterna":forms.TextInput(attrs={"class":"form-control"}),
            "descripcion": forms.Textarea(attrs={'class':'form-control', 'rows':3, 'cols':50 }),
            "componente": forms.Select(attrs={"class":"form-select"}),    
            "sistema": forms.Select(attrs={"class":"form-select"}),
            "servidor": forms.Select(attrs={"class":"form-select"}),     
            "estatus": forms.Select(attrs={"class":"form-select"}),
            "tipo": forms.Select(attrs={"class":"form-select"}),
    
        }


