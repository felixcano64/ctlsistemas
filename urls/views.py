from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from urls.forms import UrlForm
from urls.models import Url

# Create your views here.

def ok(request):
 	 return render(request,'urls/ok.html')


class UrlCreateView(LoginRequiredMixin, CreateView):
    model = Url
    form_class = UrlForm
    success_url = reverse_lazy('urls:ok')


class UrlListView(LoginRequiredMixin, ListView):
      model = Url
      queryset=Url.objects.order_by("urlInterna")
      context_object_name = "urls"

      def get_queryset(self):
        buscar = self.request.GET.get("buscar")

        if buscar:
             resultado = Url.objects.filter(urlInterna__icontains=buscar)
        else:
             resultado = Url.objects.all()

        return resultado


class UrlConsultaView(LoginRequiredMixin, UpdateView):
    model = Url
    form_class = UrlForm
    template_name = "urls/UrlCons_form.html"

class UrlUpdateView(LoginRequiredMixin, UpdateView):
    model = Url
    form_class = UrlForm
    success_url = reverse_lazy('urls:lista')