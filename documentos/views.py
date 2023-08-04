from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from documentos.forms import DocumentoForm
from documentos.models import Documento

# Create your views here.


def ok(request):
 	 return render(request,'documentos/ok.html')


class DocumentoCreateView(LoginRequiredMixin, CreateView):
    model = Documento
    form_class = DocumentoForm
    success_url = reverse_lazy('documentos:ok')

class DocumentoListView(LoginRequiredMixin, ListView):
      model = Documento
      queryset=Documento.objects.order_by("nombre")
      context_object_name = "documentos"

      def get_queryset(self):
        buscar = self.request.GET.get("buscar")

        if buscar:
             resultado = Documento.objects.filter(nombre__icontains=buscar)
        else:
             resultado = Documento.objects.all()

        return resultado

class DocumentoConsultaView(LoginRequiredMixin, UpdateView):
    model = Documento
    form_class = DocumentoForm
    template_name = "documentos/DocumentoCons_form.html"

class DocumentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Documento
    form_class = DocumentoForm
    success_url = reverse_lazy('documentos:lista')