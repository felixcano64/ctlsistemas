from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Url

# Register your models here.

class UrlResourse(resources.ModelResource):
    
    fields = ('__all__')

    class Meta:
        model = Url
        exclude = ('created_at','updated_at',)


class UrlAdmin(ImportExportModelAdmin):
    resource_class = UrlResourse

    list_display = (
        'id',
        'urlInterna',
        'componente',
        'servidor',
    )
            
    search_fields = ('urlInterna', 'componente')
    list_filter = ('servidor',)
    list_per_page = 15
    
admin.site.register(Url,UrlAdmin)