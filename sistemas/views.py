from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from sistemas.models import Sistema
from .forms import SistemaForm

# Create your views here.

def lista(request):
    
    sistemas = Sistema.objects.order_by('id').all()
    context = {
        'sistemas' : sistemas
    }
    
    return render(request,'sistemas/lista.html', context=context)


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
 	 return render(request,'sistemas/ok.html')


class SistemaCreateView(CreateView):
    model = Sistema
    form_class = SistemaForm
    #template_name = "TEMPLATE_NAME"
    #fields="__all__"
    success_url = reverse_lazy('sistemas:ok')
