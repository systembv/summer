from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Estoque
from import_export import resources



class EstoqueResource(resources.ModelResource):
    class Meta:
        model = Estoque
        ordering = ["item"]


class EstoqueAdmin(ImportExportModelAdmin):
    resource_class = EstoqueResource
    list_display = ["item"]
    #list_filter = ["nome"]

admin.site.register(Estoque, EstoqueAdmin)

