
from django.contrib import admin

from .models import Diagrama

# Register your models here.

class DiagramaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'tipo',
    )
            
    search_fields = ('nombre',)
    list_filter = ('tipo',)
    list_per_page = 15
    
admin.site.register(Diagrama,DiagramaAdmin)

