from typing import Any
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from sistemas.models import Sistema
from .forms import SistemaForm

# Create your views here.

# def lista(request):
    
#     sistemas = Sistema.objects.order_by('id').all()
#     context = {
#         'sistemas' : sistemas
#     }
    
#     return render(request,'sistemas/lista.html', context=context)


# def agregar(request):

# 	if request.method == "POST":
# 		form = SistemaForm(request.POST)
		
# 		if form.is_valid():
# 			print(form.cleaned_data)
# 			form.save()
# 			return redirect(reverse('sistemas:ok'))

# 	else:
# 		form = SistemaForm()

# 	return render(request,"sistemas/agregar.html", context={ "form":form })

def ok(request):
    context = {
        "siguiente":"/sistemas/",
        "registro":"Sistema"
    }
    
    return render(request,'ok.html', context=context)


class SistemaCreateView(LoginRequiredMixin,CreateView):
    model = Sistema
    form_class = SistemaForm
    #template_name = "TEMPLATE_NAME"
    #fields="__all__"
    success_url = reverse_lazy('sistemas:ok')

class SistemaListView(LoginRequiredMixin,ListView):
      model = Sistema
      paginate_by = 5 
      context_object_name = "sistemas"

      def get_queryset(self):
        buscar = self.request.GET.get("buscar")

        if buscar:
             resultado = Sistema.objects.filter(nombre__icontains=buscar)
        else:
             resultado = Sistema.objects.all()

        return resultado



class SistemaConsultaView(LoginRequiredMixin,UpdateView):
    model = Sistema
    form_class = SistemaForm
    template_name = "sistemas/SistemaCons_form.html"

class SistemaUpdateView(LoginRequiredMixin,UpdateView):
    model = Sistema
    form_class = SistemaForm
    success_url = reverse_lazy('sistemas:lista')
