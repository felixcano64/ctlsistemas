from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from diagramas.forms import DiagramaForm
from diagramas.models import Diagrama

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

      def get_queryset(self):
        buscar = self.request.GET.get("buscar")

        if buscar:
             resultado = Diagrama.objects.filter(nombre__icontains=buscar)
        else:
             resultado = Diagrama.objects.all()

        return resultado

class DiagramaConsultaView(LoginRequiredMixin, UpdateView):
    model = Diagrama
    form_class = DiagramaForm
    template_name = "diagramas/DiagramaCons_form.html"

class DiagramaUpdateView(LoginRequiredMixin, UpdateView):
    model = Diagrama
    form_class = DiagramaForm
    success_url = reverse_lazy('diagrama:lista')