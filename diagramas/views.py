from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from diagramas.forms import DiagramaForm, ConsultaDiagramaForm
from diagramas.models import Diagrama

import os.path

# Create your views here.

def ok(request):
    context = {
        "siguiente":"/diagramas/",
        "registro":"Diagrama"
    }
    
    return render(request,'ok.html', context=context)


class DiagramaCreateView(LoginRequiredMixin, CreateView):
    model = Diagrama
    form_class = DiagramaForm
    success_url = reverse_lazy('diagramas:ok')


class DiagramaListView(LoginRequiredMixin, ListView):
      model = Diagrama
      queryset=Diagrama.objects.order_by("nombre")
      context_object_name = "diagramas"
      paginate_by = 3

      def get_queryset(self):
        buscar = self.request.GET.get("buscar")

        if buscar:
             resultado = Diagrama.objects.filter(nombre__icontains=buscar)
        else:
             resultado = Diagrama.objects.all()

        return resultado

class DiagramaConsultaView(LoginRequiredMixin, UpdateView):
    model = Diagrama
    form_class = ConsultaDiagramaForm
    template_name = "diagramas/DiagramaCons_form.html"

    def get_context_data(self, **kwargs):

        llave = self.kwargs['pk']

        doc = Diagrama.objects.get(id=llave)
        archivo = doc.archivo

        if archivo :
            ext = os.path.splitext(archivo.name)[1]
        else:
            ext = ""

        context = super().get_context_data(**kwargs)
        context["tipo_archivo"] = ext
        context["id"] = llave
        context["archivo"] = archivo

        return context


class DiagramaUpdateView(LoginRequiredMixin, UpdateView):
    model = Diagrama
    form_class = DiagramaForm
    success_url = reverse_lazy('diagrama:lista')