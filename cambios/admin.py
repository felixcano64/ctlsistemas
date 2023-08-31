from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Cambio

# Register your models here.
class CambioResourse(resources.ModelResource):
    
    fields = ('__all__')

    class Meta:
        model = Cambio
        exclude = ('created_at','updated_at',)


class CambioAdmin(ImportExportModelAdmin):

    resource_class = CambioResourse

    list_display = (
        'id',
        'numero',
        'nombre',
        'tipo',
        'fechaCambio',
    )
            
    search_fields = ('numero', 'nombre')
    list_filter = ('tipo',)
    list_per_page = 15
    
admin.site.register(Cambio,CambioAdmin)
