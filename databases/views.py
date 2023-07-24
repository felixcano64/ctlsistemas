from django.http.response import HttpResponse
from django.shortcuts import render

from databases.models import Database

# Create your views here.

def lista(request):

    databases = Database.objects.order_by('id').all()
    context = {
        'databases' : databases
    }
    
    return render(request,'databases/lista.html', context=context)
