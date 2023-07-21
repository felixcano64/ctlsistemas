from django.http.response import HttpResponse
from django.shortcuts import render

from diagramas.models import Diagrama

# Create your views here.

def lista(request):

    diagramas = Diagrama.objects.order_by('id').all()
    context = {
        'diagramas' : diagramas
    }
    
    return render(request,'diagramas/lista.html', context=context)
