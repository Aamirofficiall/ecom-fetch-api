from django.contrib import admin
from .models import *

class CompetitorLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
    list_display_links = ('name', 'id')
    readonly_fields=('name',)

    
admin.site.register(CompetitorLink,CompetitorLinkAdmin)