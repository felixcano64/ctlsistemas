from django.db import models

from componentes.models import Componente
from smaxs.models import Smax

# Create your models here.

TIPO = (
    (1,"Menor"),
    (2,"Mayo"),
    (3,"Urgente"),
    (4,"Standar"),
)

RESULTADO = (
    (1,"Inscrito"),
    (2,"Aprobado"),   
    (3,"Cerrado"),
    (4,"Cancelado"),
    (5,"Rechazado"),
)


class Cambio(models.Model):
    numero = models.CharField("Numero", max_length=10, null=True, blank=True)
    nombre = models.CharField("Nombre", max_length=150, null=True, blank=True)
    tipo = models.IntegerField("Tipo", choices = TIPO, default = '1'  )
    descripcion = models.TextField("Descripcion", null=True, blank=True)
    fechaInscripcion = models.DateField("Fecha de Inscripcion", null=True, blank=True)
    fechaCambio = models.DateField("Fecha del Cambio", null=True, blank=True)
    aplico = models.CharField("Quin Aplico", max_length=150, null=True, blank=True)
    resultado = models.IntegerField("Resultado", choices = RESULTADO, default = '1'  )
    observacion = models.TextField("Observaciones", null=True, blank=True)
    componente = models.ForeignKey(Componente,  on_delete=models.CASCADE,  default = '1')
    smax = models.ForeignKey(Smax,  on_delete=models.CASCADE,  default = '1')  
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True) 


    class Meta:
        verbose_name = 'Cambio'
        verbose_name_plural = 'Cambios'
        ordering = ['numero','nombre']

    def __str__(self):
        return self.numero + " " + self.nombre
