from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView
from diagramas.forms import DiagramaForm

from diagramas.models import Diagrama

# Create your views here.

def ok(request):
 	 return render(request,'diagramas/ok.html')


class DiagramaCreateView(CreateView):
    model = Diagrama
    form_class = DiagramaForm
    success_url = reverse_lazy('diagramas:ok')


class DiagramaListView(ListView):
      model = Diagrama
      queryset=Diagrama.objects.order_by("nombre")
      context_object_name = "diagramas"

class DiagramaConsultaView(UpdateView):
    model = Diagrama
    form_class = DiagramaForm
    template_name = "diagramas/DiagramaCons_form.html"