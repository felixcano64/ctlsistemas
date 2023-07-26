from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from smaxs.forms import SmaxForm

from smaxs.models import Smax

# Create your views here.

def lista(request):

    smaxs = Smax.objects.order_by('id').all()
    context = {
        'smaxs' : smaxs
    }
    
    return render(request,'smaxs/lista.html', context=context)


def ok(request):
 	 return render(request,'smaxs/ok.html')


class SmaxCreateView(CreateView):
    model = Smax
    form_class = SmaxForm
    success_url = reverse_lazy('smaxs:ok')