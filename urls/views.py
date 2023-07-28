from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView
from urls.forms import UrlForm
from urls.models import Url

# Create your views here.

def ok(request):
 	 return render(request,'urls/ok.html')


class UrlCreateView(CreateView):
    model = Url
    form_class = UrlForm
    success_url = reverse_lazy('urls:ok')


class UrlListView(ListView):
      model = Url
      queryset=Url.objects.order_by("urlInterna")
      context_object_name = "urls"


class UrlConsultaView(UpdateView):
    model = Url
    form_class = UrlForm
    template_name = "urls/UrlCons_form.html"