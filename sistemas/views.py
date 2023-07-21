from django.http.response import HttpResponse
from django.shortcuts import render

from sistemas.models import Sistema

# Create your views here.

def lista(request):
    
    sistemas = Sistema.objects.order_by('id').all()
    context = {
        'sistemas' : sistemas
    }
    
    return render(request,'sistemas/lista.html', context=context)
 