from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from servidores.forms import ServidorForm
from servidores.models import Servidor


# Create your views here.

def ok(request):
    context = {
        "siguiente":"/servidores/",
        "registro":"Servidor"
    }
    
    return render(request,'ok.html', context=context)


class ServidorCreateView(LoginRequiredMixin, CreateView):
    model = Servidor
    form_class = ServidorForm
    success_url = reverse_lazy('servidores:ok')

class ServidorListView(LoginRequiredMixin, ListView):
      model = Servidor
      queryset=Servidor.objects.order_by("nombre","ip")
      context_object_name = "servidores"
      paginate_by = 3

      def get_queryset(self):
        buscar = self.request.GET.get("buscar")

        if buscar:
             resultado = Servidor.objects.filter(nombre__icontains=buscar)
        else:
             resultado = Servidor.objects.all()

        return resultado

class ServidorConsultaView(LoginRequiredMixin, UpdateView):
    model = Servidor
    form_class = ServidorForm
    template_name = "servidores/ServidorCons_form.html"

class ServidorUpdateView(LoginRequiredMixin, UpdateView):
    model = Servidor
    form_class = ServidorForm
    success_url = reverse_lazy('servidores:lista')