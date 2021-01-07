from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Compras
from import_export import resources



class ComprasResource(resources.ModelResource):
    class Meta:
        model = Compras
        ordering = ["nome"]


class ComprasAdmin(ImportExportModelAdmin):
    resource_class = ComprasResource
    list_display = ["nome"]
    #list_filter = ["nome"]

admin.site.register(Compras, ComprasAdmin)


