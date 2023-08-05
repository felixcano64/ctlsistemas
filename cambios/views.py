from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from cambios.forms import CambioForm
from cambios.models import Cambio

# Create your views here.

def ok(request):
    context = {
        "siguiente":"/cambios/",
        "registro":"Cambio"
    }
    
    return render(request,'ok.html', context=context)


class CambioCreateView(LoginRequiredMixin,CreateView):
    model = Cambio
    form_class = CambioForm
    success_url = reverse_lazy('cambios:ok')

class CambioListView(LoginRequiredMixin,ListView):
      model = Cambio
      queryset=Cambio.objects.order_by("numero")
      context_object_name = "cambios"

      def get_queryset(self):
        buscar = self.request.GET.get("buscar")

        if buscar:
             resultado = Cambio.objects.filter(nombre__icontains=buscar)
        else:
             resultado = Cambio.objects.all()

        return resultado

      

class CambioConsultaView(LoginRequiredMixin,UpdateView):
    model = Cambio
    form_class = CambioForm
    template_name = "cambios/CambioCons_form.html"


class CambioUpdateView(LoginRequiredMixin,UpdateView):
    model = Cambio
    form_class = CambioForm
    success_url = reverse_lazy('cambios:lista')
