from django.http.response import HttpResponse
from django.shortcuts import render
from urls.models import Url

# Create your views here.

def lista(request):

    urls = Url.objects.order_by('id').all()
    context = {
        'urls' : urls
    }
    
    return render(request,'urls/lista.html', context=context)

