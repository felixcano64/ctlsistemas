
from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Componente

# Register your models here.


class ComponenteResourse(resources.ModelResource):
    
    fields = ('__all__')

    class Meta:
        model = Componente
        exclude = ('created_at','updated_at',)

class ComponenteAdmin(ImportExportModelAdmin):
    resource_class = ComponenteResourse

    list_display = (
        'id',
        'nombreCorto',
        'version',
        'tipo',
        'sistema',
    )
            
    search_fields = ('nombreCorto', 'nombreLargo')
    list_filter = ('tipo',)
    list_per_page = 15
    
admin.site.register(Componente,ComponenteAdmin)
