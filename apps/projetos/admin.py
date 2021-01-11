from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Projetos
from import_export import resources



class ProjetosResource(resources.ModelResource):
    class Meta:
        model = Projetos
        ordering = ["nome"]


class ProjetosAdmin(ImportExportModelAdmin):
    resource_class = ProjetosResource
    list_display = ["nome"]
    #list_filter = ["nome"]

admin.site.register(Projetos, ProjetosAdmin)

