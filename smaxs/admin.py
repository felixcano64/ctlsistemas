from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Smax

# Register your models here.

class SmaxResourse(resources.ModelResource):
    
    fields = ('__all__')

    class Meta:
        model = Smax
        exclude = ('created_at','updated_at',)

class SmaxAdmin(ImportExportModelAdmin):
    resource_class = SmaxResourse

    list_display = (
        'id',
        'numero',
        'fechaCompromiso',
        'estatus',
    )
            
    search_fields = ('numero', 'descripcion')
    list_filter = ('estatus',)
    list_per_page = 15
    
admin.site.register(Smax,SmaxAdmin)