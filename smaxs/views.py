from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from smaxs.forms import SmaxForm
from smaxs.models import Smax

# Create your views here.

def ok(request):
 	 return render(request,'smaxs/ok.html')


class SmaxCreateView(LoginRequiredMixin, CreateView):
    model = Smax
    form_class = SmaxForm
    success_url = reverse_lazy('smaxs:ok')


class SmaxListView(LoginRequiredMixin, ListView):
      model = Smax
      queryset=Smax.objects.order_by("numero")
      context_object_name = "smaxs"

      def get_queryset(self):
        buscar = self.request.GET.get("buscar")

        if buscar:
             resultado = Smax.objects.filter(numero__icontains=buscar)
        else:
             resultado = Smax.objects.all()

        return resultado

class SmaxConsultaView(LoginRequiredMixin, UpdateView):
    model = Smax
    form_class = SmaxForm
    template_name = "smaxs/SmaxCons_form.html"

class SmaxUpdateView(LoginRequiredMixin, UpdateView):
    model = Smax
    form_class = SmaxForm
    success_url = reverse_lazy('smaxs:lista')