from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from componentes.forms import ComponenteForm
from componentes.models import Componente

# Create your views here.

def lista(request):

    componentes = Componente.objects.order_by('id').all()
    context = {
        'componentes' : componentes
    }
    
    return render(request,'componentes/lista.html', context=context)


def ok(request):
 	 return render(request,'componentes/ok.html')


class ComponenteCreateView(CreateView):
    model = Componente
    form_class = ComponenteForm
    success_url = reverse_lazy('componentes:ok')