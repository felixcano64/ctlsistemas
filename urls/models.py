from django.db import models

from componentes.models import Componente
from servidores.models import Servidor

# Create your models here.

class Url(models.Model):
    urlInterna = models.CharField("Url Interna", max_length=250, null=True, blank=True)
    urlExterna = models.CharField("Url Externa", max_length=250, null=True, blank=True)
    descripcion = models.TextField("Descripcion", null=True, blank=True)
    estatus = models.IntegerField("Estatus",null=True, blank=True)
    componente = models.ForeignKey(Componente,  on_delete=models.CASCADE, null=False, blank=False)     
    servidor = models.ForeignKey(Servidor,  on_delete=models.CASCADE, null=False, blank=False)       
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True)
    
    
    class Meta:
        verbose_name = 'url'
        verbose_name_plural = 'urls'

    def __str__(self):
        return self.utlInterna
