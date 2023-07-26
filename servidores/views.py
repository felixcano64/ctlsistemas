from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from servidores.forms import ServidorForm

from servidores.models import Servidor


# Create your views here.

def lista(request):

    servidores = Servidor.objects.order_by('id').all()
    context = {
        'servidores' : servidores
    }
    
    return render(request,'servidores/lista.html', context=context)

def ok(request):
 	 return render(request,'servidores/ok.html')


class ServidorCreateView(CreateView):
    model = Servidor
    form_class = ServidorForm
    success_url = reverse_lazy('servidores:ok')
