from django.contrib import admin

from .models import Servidor

# Register your models here.

class ServidorAdmin(admin.ModelAdmin):
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
