from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView
from documentos.forms import DocumentoForm

from documentos.models import Documento

# Create your views here.


def ok(request):
 	 return render(request,'documentos/ok.html')


class DocumentoCreateView(CreateView):
    model = Documento
    form_class = DocumentoForm
    success_url = reverse_lazy('documentos:ok')

class DocumentoListView(ListView):
      model = Documento
      queryset=Documento.objects.order_by("nombre")
      context_object_name = "documentos"

class DocumentoConsultaView(UpdateView):
    model = Documento
    form_class = DocumentoForm
    template_name = "documentos/DocumentoCons_form.html"