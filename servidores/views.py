from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def lista(request):
    return render(request,'servidores/lista.html')
