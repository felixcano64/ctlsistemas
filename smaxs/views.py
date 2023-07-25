from django.http.response import HttpResponse
from django.shortcuts import render

from smaxs.models import Smax

# Create your views here.

def lista(request):

    smaxs = Smax.objects.order_by('id').all()
    context = {
        'smaxs' : smaxs
    }
    
    return render(request,'smaxs/lista.html', context=context)
