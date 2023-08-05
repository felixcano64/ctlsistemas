from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView,UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from componentes.forms import ComponenteForm
from componentes.models import Componente

# Create your views here.

def ok(request):
    context = {
        "siguiente":"/componentes/",
        "registro":"Componente"
    }
    
    return render(request,'ok.html', context=context)


class ComponenteCreateView(LoginRequiredMixin, CreateView):
    model = Componente
    form_class = ComponenteForm
    success_url = reverse_lazy('componentes:ok')

class ComponenteListView(LoginRequiredMixin, ListView):
      model = Componente
      queryset=Componente.objects.order_by("nombreCorto")
      context_object_name = "componentes"

      def get_queryset(self):
        buscar = self.request.GET.get("buscar")

        if buscar:
             resultado = Componente.objects.filter(nombreCorto__icontains=buscar)
        else:
             resultado = Componente.objects.all()

        return resultado      

class ComponenteConsultaView(LoginRequiredMixin, UpdateView):
    model = Componente
    form_class = ComponenteForm
    template_name = "componentes/ComponenteCons_form.html"


class ComponenteUpdateView(LoginRequiredMixin, UpdateView):
    model = Componente
    form_class = ComponenteForm
    success_url = reverse_lazy('componentes:lista')