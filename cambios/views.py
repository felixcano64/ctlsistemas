from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from cambios.forms import CambioForm
from cambios.models import Cambio

# Create your views here.

def lista(request):

    cambios = Cambio.objects.order_by('id').all()
    context = {
        'cambios' : cambios
    }
    
    return render(request,'cambios/lista.html', context=context)

def ok(request):
 	 return render(request,'cambios/ok.html')


class CambioCreateView(CreateView):
    model = Cambio
    form_class = CambioForm
    success_url = reverse_lazy('cambios:ok')

