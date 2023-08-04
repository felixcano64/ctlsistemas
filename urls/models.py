from django.db import models

from componentes.models import Componente
from servidores.models import Servidor
from sistemas.models import Sistema


# Create your models here.

ESTATUS = (
    (1,"Activo"),
    (2,"Inactivo"),
)

TIPO = (
    (1,"Interna"),
    (2,"Externa"),
    (3,"PI-PO"),
    (4,"DataPower")
)

class Url(models.Model):
    urlInterna = models.CharField("Url Interna", max_length=250, null=True, blank=True)
    urlExterna = models.CharField("Url Externa", max_length=250, null=True, blank=True)
    descripcion = models.TextField("Descripcion", null=True, blank=True)
    tipo = models.IntegerField("Tipo", choices = TIPO, default = '1')
    estatus = models.IntegerField("Estatus", choices = ESTATUS, default = '1')
    componente = models.ForeignKey(Componente,  on_delete=models.CASCADE,  default = '1')     
    sistema = models.ForeignKey(Sistema,  on_delete=models.CASCADE, default = '1' )       
    servidor = models.ForeignKey(Servidor,  on_delete=models.CASCADE,  default = '1')       
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True)
    
    
    class Meta:
        verbose_name = 'url'
        verbose_name_plural = 'urls'

    def __str__(self):
        return self.urlInterna
