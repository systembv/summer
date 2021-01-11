from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Funcionarios
from import_export import resources



class FuncionariosResource(resources.ModelResource):
    class Meta:
        model = Funcionarios
        ordering = ["nome"]


class FuncionariosAdmin(ImportExportModelAdmin):
    resource_class = FuncionariosResource
    list_display = ["nome"]
    #list_filter = ["nome"]

admin.site.register(Funcionarios, FuncionariosAdmin)

