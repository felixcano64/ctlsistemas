from django.db import models
from servidores.models import Servidor

from sistemas.models import Sistema

# Create your models here.
class Componente(models.Model):
    nombreCorto = models.CharField("Nombre Corto", max_length=50, null=True, blank=True)
    nombreLargo = models.CharField("Nombre Largo", max_length=150, null=True, blank=True)
    descripcion = models.TextField("Descripcion", null=True, blank=True)
    version= models.CharField("Version", max_length=50, null=True, blank=True)
    lenguaje= models.CharField("Lenguaje", max_length=100, null=True, blank=True)
    tipo = models.IntegerField("Tipo",null=True, blank=True)
    estatus = models.IntegerField("Estatus",null=True, blank=True)
    sistema = models.ForeignKey(Sistema,  on_delete=models.CASCADE, null=False, blank=False) 
    servidor = models.ForeignKey(Servidor,  on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True)

    class Meta:
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'
        ordering = ['nombreCorto', 'version']
        

    def __str__(self):
        return self.nombreCorto + " " + self.version
