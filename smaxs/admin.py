from django.contrib import admin

from .models import Smax

# Register your models here.

class SmaxAdmin(admin.ModelAdmin):
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