from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from databases.forms import DatabaseForm
from databases.models import Database

# Create your views here.

def ok(request):
 	 return render(request,'databases/ok.html')

class DatabaseCreateView(CreateView):
    model = Database
    form_class = DatabaseForm
    success_url = reverse_lazy('databases:ok')

class DatabaseListView(ListView):
      model = Database
      queryset=Database.objects.order_by("nombre")
      context_object_name = "databases"

class DatabaseConsultaView(UpdateView):
    model = Database
    form_class = DatabaseForm
    template_name = "databases/DatabaseCons_form.html"