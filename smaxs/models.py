from django.db import models

from sistemas.models import Sistema

# Create your models here.

ESTATUS = (
    (1,"Activo"),
    (2,"Inactivo"),
)

TIPO = (
    (1,"Requerimiento"),
    (2,"Proyecto"),
)

class Smax(models.Model):
    numero = models.CharField("Numero", max_length=10, null=True, blank=True)
    descripcion = models.TextField("Descripcion", null=True, blank=True)
    fechaCompromiso = models.DateField("Fecha Compromiso", null=True, blank=True)
    tipo = models.IntegerField("Tipo", choices = TIPO, default = '1')
    sistema = models.ForeignKey(Sistema,  on_delete=models.CASCADE, default = '1')
    estatus = models.IntegerField("Estatus", choices = ESTATUS, default = '1')
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True)
        
    class Meta:
        verbose_name = 'Smax'
        verbose_name_plural = 'Smaxs'
        ordering = ['numero']

    def __str__(self):
        return self.numero + " " + self.descripcion

