from django.db import models

from componentes.models import Componente
from smaxs.models import Smax

# Create your models here.

class Cambio(models.Model):
    numero = models.CharField("Numero", max_length=10, null=True, blank=True)
    nombre = models.CharField("Nombre", max_length=150, null=True, blank=True)
    tipo = models.IntegerField("tipo", null=True, blank=True)
    descripcion = models.TextField("Descripcion", null=True, blank=True)
    fechaInscripcion = models.DateField("Fecha de Inscripcion", null=True, blank=True)
    fechaCambio = models.DateField("Fecha del Cambio", null=True, blank=True)
    aplico = models.CharField("Quin Aplico", max_length=150, null=True, blank=True)
    resultado = models.IntegerField("Resultado", null=True, blank=True)
    observacion = models.TextField("Observaciones", null=True, blank=True)
    componente = models.ForeignKey(Componente,  on_delete=models.CASCADE, null=False, blank=False)
    smax = models.ForeignKey(Smax,  on_delete=models.CASCADE, null=False, blank=False)  
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True) 


    class Meta:
        verbose_name = 'Cambio'
        verbose_name_plural = 'Cambios'
        ordering = ['numero','nombre']

    def __str__(self):
        return self.numero + " " + self.nombre