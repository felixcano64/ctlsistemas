from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView, UpdateView
from responsables.forms import ResponsableForm

from responsables.models import Responsable

# Create your views here.
def ok(request):
 	 return render(request,'responsables/ok.html')


class ResponsableCreateView(CreateView):
    model = Responsable
    form_class = ResponsableForm
    success_url = reverse_lazy('responsables:ok')

class ResponsableListView(ListView):
      model = Responsable
      queryset=Responsable.objects.order_by("apPaterno","apMaterno","nombre")
      context_object_name = "responsables"

class ResponsableConsultaView(UpdateView):
    model = Responsable
    form_class = ResponsableForm
    template_name = "responsables/ResponsableCons_form.html"