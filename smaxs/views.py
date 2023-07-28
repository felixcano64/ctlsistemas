from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView, UpdateView
from smaxs.forms import SmaxForm

from smaxs.models import Smax

# Create your views here.

def ok(request):
 	 return render(request,'smaxs/ok.html')


class SmaxCreateView(CreateView):
    model = Smax
    form_class = SmaxForm
    success_url = reverse_lazy('smaxs:ok')


class SmaxListView(ListView):
      model = Smax
      queryset=Smax.objects.order_by("numero")
      context_object_name = "smaxs"

class SmaxConsultaView(UpdateView):
    model = Smax
    form_class = SmaxForm
    template_name = "smaxs/SmaxCons_form.html"