from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib import admin
from .models import *



class ProductsLinkResource(resources.ModelResource):
    class Meta:
        model  = ProductsLink

        
class ProductsLinkAdmin(ImportExportModelAdmin):
    resource_classes = [ProductsLinkResource]

        
class CompetitorLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
    list_display_links = ('name', 'id')
    readonly_fields=('name',)

    
admin.site.register(CompetitorLink,CompetitorLinkAdmin)
admin.site.register(ProductsLink, ProductsLinkAdmin)
