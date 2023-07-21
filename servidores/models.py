from django.db import models

# Create your models here.

class Servidor(models.Model):
    nombre = models.CharField("Nombre", max_length=15, null=True, blank=True)
    ip = models.CharField("IP", max_length=15, null=True, blank=True)
    so = models.CharField("Sistema Operetivo", max_length=20, null=True, blank=True)
    tipo = models.IntegerField("Sistema Operetivo", null=True, blank=True)
    ambiente = models.CharField("Ambiente", max_length=20, null=True, blank=True )
    descripcion = models.TextField("Descripcion", null=True, blank=True)
    estatus = models.IntegerField("Estatus",null=True, blank=True)
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True)

    class Meta:
        verbose_name = 'Servidor'
        verbose_name_plural = 'Servidores'

    def __str__(self):
        return self.nombre + " " + self.ip
