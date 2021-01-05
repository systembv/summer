from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Unidade
from import_export import resources



class UnidadeResource(resources.ModelResource):
    class Meta:
        model = Unidade
        ordering = ["nome"]


class UnidadeAdmin(ImportExportModelAdmin):
    resource_class = UnidadeResource
    list_display = ["nome"]
    #list_filter = ["nome"]

admin.site.register(Unidade, UnidadeAdmin)

