
# from django import forms
# from responsables.models import Responsable

# class SistemasForm(forms.Form):
#     nombre = forms.CharField(label="Nombre", max_length=100, 
#                              widget=forms.TextInput(attrs={"class":"form-control"}))
    
#     siglas = forms.CharField(label="Siglas", max_length=15,
#                              widget=forms.TextInput(attrs={"class":"form-control"}))
    
#     responsable = forms.ModelChoiceField(queryset=Responsable.objects.all(), label="Responsable",
#                                          widget=forms.Select(attrs={"class":"form-select"}))
    
#     descripcion = forms.CharField(label="Descripcion", 
#                                   widget=forms.Textarea(attrs={'class':'form-control', 'row':5, 'cols':50 }))


from django import forms
from django.forms import ModelForm
from .models import Sistema


class SistemaForm(ModelForm):
    """Form definition for Sistemas."""

    class Meta:
        """Meta definition for Sistemasform."""

        model = Sistema
        fields = "__all__"

        widgets={
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "siglas": forms.TextInput(attrs={"class":"form-control"}),
            "responsable": forms.Select(attrs={"class":"form-select"}),
            "descripcion": forms.Textarea(attrs={'class':'form-control', 'rows':5, 'cols':50 }),
        }

