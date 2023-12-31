from django.db import models
from ckeditor.fields import RichTextField

from sistemas.models import Sistema

# Create your models here.

TIPO = (
    (1, "Word"),
    (2, "Excel"),
    (3, "PowerPoint"),
    (4, "PDF"),
    (5, "Email"),
    (6, "Otro"),
)

ESTATUS = (
    (1,"Activo"),
    (2,"Inactivo"),
)


class Documento(models.Model):
    nombre = models.CharField("Nombre", max_length=150, null=True, blank=True)
    descripcion = RichTextField("Descripcion", null=True, blank=True)
    archivo = models.FileField(upload_to="documentos/", null=True, blank=True ) 
    tipo = models.IntegerField("Tipo", choices = TIPO, default = '1'  )
    estatus = models.IntegerField("Estatus", choices = ESTATUS, default = '1')
    sistema = models.ForeignKey(Sistema,  on_delete=models.CASCADE, default = '1')
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True)
    
    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
