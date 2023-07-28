from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from cambios.forms import CambioForm
from cambios.models import Cambio

# Create your views here.

def ok(request):
 	 return render(request,'cambios/ok.html')


class CambioCreateView(CreateView):
    model = Cambio
    form_class = CambioForm
    success_url = reverse_lazy('cambios:ok')

class CambioListView(ListView):
      model = Cambio
      queryset=Cambio.objects.order_by("numero")
      context_object_name = "cambios"

class CambioConsultaView(UpdateView):
    model = Cambio
    form_class = CambioForm
    template_name = "cambios/CambioCons_form.html"