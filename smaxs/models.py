from django.db import models

# Create your models here.

class Smax(models.Model):
    numero = models.CharField("Numero", max_length=10, null=True, blank=True)
    descripcion = models.TextField("Descripcion", null=True, blank=True)
    fechaCompromiso = models.DateTimeField("Fecha Compromiso", null=True, blank=True)
    estatus = models.IntegerField("Estatus",null=True, blank=True)
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True)
    
    
    class Meta:
        verbose_name = 'Smax'
        verbose_name_plural = 'Smaxs'
        ordering = ['numero']

    def __str__(self):
        return self.numero + " " + self.descripcion

