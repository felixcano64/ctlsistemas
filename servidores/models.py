from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

TIPO = (
    (1, "Servidor Aplicaciones"),
    (2, "Base de Datos"),
    (3, "Publicador"),
)

AMBIENTE = (
    (1,"Desarrollo"),
    (2,"QA"),
    (3,"Produccion"),
)

SO = (
    (1,"Windows"),
    (2,"Linux"),
    (3,"Mainframe")
)

ESTATUS = (
    (1,"Activo"),
    (2,"Inactivo"),
)


class Servidor(models.Model):
    nombre = models.CharField("Nombre", max_length=15, null=True, blank=True)
    ip = models.CharField("IP", max_length=15, null=True, blank=True)
    so = models.IntegerField("Sistema Operetivo", choices = SO, default = '1' )
    tipo = models.IntegerField("Tipo", choices = TIPO, default = '1'  )
    ambiente = models.IntegerField("Ambiente", choices = AMBIENTE, default = '1'  )
    descripcion = RichTextField("Descripcion", null=True, blank=True)
    estatus = models.IntegerField("Estatus", choices = ESTATUS, default = '1')
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True)

    class Meta:
        verbose_name = 'Servidor'
        verbose_name_plural = 'Servidores'

    def __str__(self):
        return self.nombre + " / " + self.ip
