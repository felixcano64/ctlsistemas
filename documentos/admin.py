
from django.contrib import admin

from .models import Documento

# Register your models here.

class DocumentoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
    )
            
    search_fields = ('nombre',)
    list_per_page = 15
    
admin.site.register(Documento,DocumentoAdmin)