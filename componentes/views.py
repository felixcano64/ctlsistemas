from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView,UpdateView

from componentes.forms import ComponenteForm
from componentes.models import Componente

# Create your views here.

def ok(request):
 	 return render(request,'componentes/ok.html')


class ComponenteCreateView(CreateView):
    model = Componente
    form_class = ComponenteForm
    success_url = reverse_lazy('componentes:ok')

class ComponenteListView(ListView):
      model = Componente
      queryset=Componente.objects.order_by("nombreCorto")
      context_object_name = "componentes"

class ComponenteConsultaView(UpdateView):
    model = Componente
    form_class = ComponenteForm
    template_name = "componentes/ComponenteCons_form.html"