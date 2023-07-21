from django.db import models

from sistemas.models import Sistema

# Create your models here.

class Documento(models.Model):
    nombre = models.CharField("Nombre", max_length=150, null=True, blank=True)
    descripcion = models.TextField("Descripcion", null=True, blank=True)
    path= models.CharField("Path", max_length=200, null=True, blank=True)
    estatus = models.IntegerField("Estatus",null=True, blank=True)
    sistema = models.ForeignKey(Sistema,  on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True)
    
    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
