from django.contrib import admin

from .models import Cambio

# Register your models here.

class CambioAdmin(admin.ModelAdmin):
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
