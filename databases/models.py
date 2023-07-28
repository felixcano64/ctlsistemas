from django.db import models

from servidores.models import Servidor

# Create your models here.
class Database(models.Model):
    nombre = models.CharField("Nombre", max_length=30, null=True, blank=True)
    manejador = models.CharField("Manejador", max_length=50, null=True, blank=True)
    usuario = models.CharField("Usuario", max_length=30, null=True, blank=True)
    password = models.CharField("Password", max_length=30, null=True, blank=True)
    puerto = models.CharField("Puerto", max_length=6, null=True, blank=True)
    servidor = models.ForeignKey(Servidor,  on_delete=models.CASCADE,  default = '1')
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True)


    class Meta:
        verbose_name = 'Database'
        verbose_name_plural = 'Databases'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
