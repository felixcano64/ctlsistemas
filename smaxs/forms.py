
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm
from .models import Smax

# class DateTimeInput(forms.DateTimeInput):
#     input_type = 'date'

class SmaxForm(ModelForm):

    class Meta:
        model = Smax
        fields = "__all__"

        widgets={
            "numero": forms.TextInput(attrs={"class":"form-control"}), 
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "descripcion": forms.Textarea(attrs={'class':'form-control', 'rows':3, 'cols':50 }),
            "fechaCompromiso": AdminDateWidget(),
            # "fechaCompromiso": DateTimeInput(),
            "tipo": forms.Select(attrs={"class":"form-select"}),
            "sistema": forms.Select(attrs={"class":"form-select"}),
            "estatus": forms.Select(attrs={"class":"form-select"}),
        }


