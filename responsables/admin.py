from django.contrib import admin

from .models import Responsable

# Register your models here.

class ResponsableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apPaterno',
        'apMaterno',
        'area',
        'puesto',
    )
            
    search_fields = ('nombre','apPaterno','apMaterno')
    list_filter = ('area','puesto')
    list_per_page = 15
    
admin.site.register(Responsable,ResponsableAdmin)
