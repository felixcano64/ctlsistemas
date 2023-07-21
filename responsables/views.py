from django.http.response import HttpResponse
from django.shortcuts import render

from responsables.models import Responsable

# Create your views here.

def lista(request):
    
    responsables = Responsable.objects.order_by('id').all()
    context = {
        'responsables' : responsables
    }
    
    return render(request,'responsables/lista.html', context=context)
