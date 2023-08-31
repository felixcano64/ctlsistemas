from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Sistema

# Register your models here.

class SistemaResourse(resources.ModelResource):
    
    fields = ('__all__')

    class Meta:
        model = Sistema
        exclude = ('created_at','updated_at',)

class SistemaAdmin(ImportExportModelAdmin):
    resource_class = SistemaResourse

    list_display = (
        'id',
        'nombre',
        'responsable',
    )
            
    search_fields = ('nombre',)
    list_filter = ('responsable',)
    list_per_page = 15
    
admin.site.register(Sistema,SistemaAdmin)
