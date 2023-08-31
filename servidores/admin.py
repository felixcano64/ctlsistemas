from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Servidor

# Register your models here.

class ServidorResourse(resources.ModelResource):
    
    fields = ('__all__')

    class Meta:
        model = Servidor
        exclude = ('created_at','updated_at',)

class ServidorAdmin(ImportExportModelAdmin):
    resource_class = ServidorResourse
    
    list_display = (
        'id',
        'nombre',
        'ip',
        'tipo',
        'so',
        'ambiente',
    )
            
    search_fields = ('nombre', 'ip')
    list_filter = ('tipo', 'so', 'ambiente')
    list_per_page = 15
    
admin.site.register(Servidor,ServidorAdmin)
