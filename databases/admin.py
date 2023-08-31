
from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Database

# Register your models here.

class DatabaseResourse(resources.ModelResource):
    
    fields = ('__all__')

    class Meta:
        model = Database
        exclude = ('created_at','updated_at',)


class DatabaseAdmin(ImportExportModelAdmin):
    resource_class = DatabaseResourse

    list_display = (
        'id',
        'nombre',
        'manejador',
        'servidor'
    )
            
    search_fields = ('nombre', 'manejador','servidor')
    list_filter = ('servidor',)
    list_per_page = 15
    
admin.site.register(Database,DatabaseAdmin)