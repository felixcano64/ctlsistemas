from django.db import models
from databases.models import Database
from servidores.models import Servidor
from sistemas.models import Sistema

# Create your models here.

TIPO = (
    (1, "Programa"),
    (2, "Web Services"),
    (3, "Api"),
    (4,"Scipt")
)

ESTATUS = (
    (1,"Activo"),
    (2,"Inactivo"),
)



class Componente(models.Model):
    nombreCorto = models.CharField("Nombre Corto", max_length=50, null=True, blank=True)
    nombreLargo = models.CharField("Nombre Largo", max_length=150, null=True, blank=True)
    descripcion = models.TextField("Descripcion", null=True, blank=True)
    version= models.CharField("Version", max_length=50, null=True, blank=True)
    tipo = models.IntegerField("Tipo", choices = TIPO, default = '1'  )
    estatus = models.IntegerField("Estatus", choices = ESTATUS, default = '1')
    sistema = models.ForeignKey(Sistema,  on_delete=models.CASCADE, null=False, blank=False) 
    servidor = models.ForeignKey(Servidor,  on_delete=models.CASCADE, null=False, blank=False)    
    database = models.ForeignKey(Database,  on_delete=models.CASCADE, null=False, blank=False)    
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("modificado", auto_now=True)

    class Meta:
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'
        ordering = ['nombreCorto', 'version']
        

    def __str__(self):
        return self.nombreCorto + " " + self.version
