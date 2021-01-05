from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Pecas
from import_export import resources



class PecasResource(resources.ModelResource):
    class Meta:
        model = Pecas
        ordering = ["nome"]


class PecasAdmin(ImportExportModelAdmin):
    resource_class = PecasResource
    list_display = ["nome", "unidade"]
    #list_filter = ["nome"]

admin.site.register(Pecas, PecasAdmin)
