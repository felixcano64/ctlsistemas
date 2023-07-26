from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from urls.forms import UrlForm
from urls.models import Url

# Create your views here.

def lista(request):

    urls = Url.objects.order_by('id').all()
    context = {
        'urls' : urls
    }
    
    return render(request,'urls/lista.html', context=context)


def ok(request):
 	 return render(request,'urls/ok.html')


class UrlCreateView(CreateView):
    model = Url
    form_class = UrlForm
    success_url = reverse_lazy('urls:ok')

