from django.http.response import HttpResponse
from django.shortcuts import render

from servidores.models import Servidor


# Create your views here.

def lista(request):

    servidores = Servidor.objects.order_by('id').all()
    context = {
        'servidores' : servidores
    }
    
    return render(request,'servidores/lista.html', context=context)
