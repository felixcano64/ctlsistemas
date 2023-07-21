
from django.contrib import admin

from .models import Componente

# Register your models here.

class ComponenteAdmin(admin.ModelAdmin):
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
