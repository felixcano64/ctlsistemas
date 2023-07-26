from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from documentos.forms import DocumentoForm

from documentos.models import Documento

# Create your views here.

def lista(request):

    documentos = Documento.objects.order_by('id').all()
    context = {
        'documentos' : documentos
    }
    
    return render(request,'documentos/lista.html', context=context)


def ok(request):
 	 return render(request,'documentos/ok.html')


class DocumentoCreateView(CreateView):
    model = Documento
    form_class = DocumentoForm
    success_url = reverse_lazy('documentos:ok')


