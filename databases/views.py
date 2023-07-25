from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from databases.forms import DatabaseForm
from databases.models import Database

# Create your views here.

def lista(request):

    databases = Database.objects.order_by('id').all()
    context = {
        'databases' : databases
    }
    
    return render(request,'databases/lista.html', context=context)


def ok(request):
 	 return render(request,'databases/ok.html')


class DatabaseCreateView(CreateView):
    model = Database
    form_class = DatabaseForm
    success_url = reverse_lazy('databases:ok')
