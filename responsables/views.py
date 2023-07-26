from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from responsables.forms import ResponsableForm

from responsables.models import Responsable

# Create your views here.

def lista(request):
    
    responsables = Responsable.objects.order_by('id').all()
    context = {
        'responsables' : responsables
    }
    
    return render(request,'responsables/lista.html', context=context)

def ok(request):
 	 return render(request,'responsables/ok.html')


class ResponsableCreateView(CreateView):
    model = Responsable
    form_class = ResponsableForm
    success_url = reverse_lazy('responsables:ok')
