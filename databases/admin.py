
from django.contrib import admin

from .models import Database

# Register your models here.

class DatabaseAdmin(admin.ModelAdmin):
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