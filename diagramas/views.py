from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from diagramas.forms import DiagramaForm

from diagramas.models import Diagrama

# Create your views here.

def lista(request):

    diagramas = Diagrama.objects.order_by('id').all()
    context = {
        'diagramas' : diagramas
    }
    
    return render(request,'diagramas/lista.html', context=context)



def ok(request):
 	 return render(request,'diagramas/ok.html')


class DiagramaCreateView(CreateView):
    model = Diagrama
    form_class = DiagramaForm
    success_url = reverse_lazy('diagramas:ok')

