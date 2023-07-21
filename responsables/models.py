from django.db import models

# Create your models here.

class Responsable(models.Model):
    nombre = models.CharField("Nombre", max_length=60, null=True, blank=True)
    apPaterno = models.CharField("Ap. Paterno", max_length=50, null=True, blank=True)
    apMaterno = models.CharField("Ap. Materno", max_length=50, null=True, blank=True)
    area = models.CharField("Area", max_length=150, null=True, blank=True)
    puesto = models.CharField("Puesto", max_length=150, null=True, blank=True)
    email = models.EmailField("Email", max_length=150, null=True, blank=True )
    telefono = models.CharField("Telefono", max_length=20, null=True, blank=True)
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True)

    class Meta:
        verbose_name = 'Responsable'
        verbose_name_plural = 'Responsables'
        ordering = ['apPaterno', 'apMaterno', 'nombre']


    def __str__(self):
        return self.nombre + " " + self.apPaterno + " " + self.apMaterno
