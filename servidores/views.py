from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView
from servidores.forms import ServidorForm

from servidores.models import Servidor


# Create your views here.

def ok(request):
 	 return render(request,'servidores/ok.html')


class ServidorCreateView(CreateView):
    model = Servidor
    form_class = ServidorForm
    success_url = reverse_lazy('servidores:ok')

class ServidorListView(ListView):
      model = Servidor
      queryset=Servidor.objects.order_by("nombre","ip")
      context_object_name = "servidores"

class ServidorConsultaView(UpdateView):
    model = Servidor
    form_class = ServidorForm
    template_name = "servidores/ServidorCons_form.html"