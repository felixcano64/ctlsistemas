from django.contrib import admin

from .models import Sistema

# Register your models here.

class SistemaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'responsable',
    )
            
    search_fields = ('nombre',)
    list_filter = ('responsable',)
    list_per_page = 15
    
admin.site.register(Sistema,SistemaAdmin)
