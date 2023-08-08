from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from databases.forms import DatabaseForm
from databases.models import Database

# Create your views here.

def ok(request):
    context = {
        "siguiente":"/databases/",
        "registro":"Database"
    }
    
    return render(request,'ok.html', context=context)

class DatabaseCreateView(LoginRequiredMixin, CreateView):
    model = Database
    form_class = DatabaseForm
    success_url = reverse_lazy('databases:ok')

class DatabaseListView(LoginRequiredMixin, ListView):
      model = Database
      queryset=Database.objects.order_by("nombre")
      context_object_name = "databases"
      paginate_by = 3

      def get_queryset(self):
        buscar = self.request.GET.get("buscar")

        if buscar:
             resultado = Database.objects.filter(nombre__icontains=buscar)
        else:
             resultado = Database.objects.all()

        return resultado

class DatabaseConsultaView(LoginRequiredMixin, UpdateView):
    model = Database
    form_class = DatabaseForm
    template_name = "databases/DatabaseCons_form.html"

class DatabaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Database
    form_class = DatabaseForm
    success_url = reverse_lazy('database:lista')