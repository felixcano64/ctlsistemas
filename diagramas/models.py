from django.db import models
from ckeditor.fields import RichTextField

from sistemas.models import Sistema

# Create your models here.
TIPO = (
    (1, "Diagrama"),
    (2, "Descripcion"),
    (3, "Metodologia"),
)

ESTATUS = (
    (1,"Activo"),
    (2,"Inactivo"),
)


class Diagrama(models.Model):
    nombre = models.CharField("Nombre", max_length=150, null=True, blank=True)
    descripcion = RichTextField("Descripcion", null=True, blank=True)
    archivo = models.FileField(upload_to="diagramas/", null=True, blank=True ) 
    tipo = models.IntegerField("Tipo", choices = TIPO, default = '1'  )
    estatus = models.IntegerField("Estatus", choices = ESTATUS, default = '1')
    sistema = models.ForeignKey(Sistema,  on_delete=models.CASCADE,  default = '1')
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True)

    class Meta:
        verbose_name = 'Diagrama'
        verbose_name_plural = 'Diagramas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre