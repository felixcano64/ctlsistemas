from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q 

from responsables.forms import ResponsableForm
from responsables.models import Responsable

# Create your views here.
def ok(request):
 	 return render(request,'responsables/ok.html')


class ResponsableCreateView(LoginRequiredMixin, CreateView):
    model = Responsable
    form_class = ResponsableForm
    success_url = reverse_lazy('responsables:ok')

class ResponsableListView(LoginRequiredMixin, ListView):
      model = Responsable
      queryset=Responsable.objects.order_by("apPaterno","apMaterno","nombre")
      context_object_name = "responsables"

      def get_queryset(self):
        buscar = self.request.GET.get("buscar")

        if buscar:
             resultado = Responsable.objects.filter(Q(nombre__icontains=buscar) | Q(apPaterno__icontains=buscar) |  Q(apMaterno__icontains=buscar) )
        else:
             resultado = Responsable.objects.all()

        return resultado

class ResponsableConsultaView(LoginRequiredMixin, UpdateView):
    model = Responsable
    form_class = ResponsableForm
    template_name = "responsables/ResponsableCons_form.html"

class ResponsableUpdateView(LoginRequiredMixin, UpdateView):
    model = Responsable
    form_class = ResponsableForm
    success_url = reverse_lazy('responsables:lista')