from django.http.response import HttpResponse
from django.shortcuts import render

from documentos.models import Documento

# Create your views here.

def lista(request):

    documentos = Documento.objects.order_by('id').all()
    context = {
        'documentos' : documentos
    }
    
    return render(request,'documentos/lista.html', context=context)

