from django.http.response import HttpResponse
from django.shortcuts import render

from componentes.models import Componente

# Create your views here.

def lista(request):

    componentes = Componente.objects.order_by('id').all()
    context = {
        'componentes' : componentes
    }
    
    return render(request,'componentes/lista.html', context=context)