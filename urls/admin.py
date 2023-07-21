from django.contrib import admin

from .models import Url

# Register your models here.

class UrlAdmin(admin.ModelAdmin):
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