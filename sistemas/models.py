from django.db import models

from responsables.models import Responsable

# Create your models here.

class Sistema(models.Model):
    nombre = models.CharField("Nombre", max_length=100, null=False, blank=False)
    descripcion = models.TextField("Descripcion", null=True, blank=True)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE, null=False, blank=False) 
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True)

    class Meta:
        verbose_name = "Sistema"
        verbose_name_plural = "Sistemas"
        ordering = ['nombre']


    def __str__(self):
        return str(self.nombre)
    
