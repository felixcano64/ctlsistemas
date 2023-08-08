from django.db import models

from ckeditor.fields import RichTextField

from responsables.models import Responsable

# Create your models here.

class Sistema(models.Model):
    nombre = models.CharField("Nombre", max_length=100, null=False, blank=False)
    siglas = models.CharField("Siglas", max_length=15, null=True, blank=True, default = '')
    descripcion = RichTextField("Descripcion", null=True, blank=True)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE, default = '1') 
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True)

    class Meta:
        verbose_name = "Sistema"
        verbose_name_plural = "Sistemas"
        ordering = ['nombre']

    def __str__(self):
        return str(self.nombre)
    
