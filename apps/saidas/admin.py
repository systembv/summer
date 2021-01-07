from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Saidas
from import_export import resources



class SaidasResource(resources.ModelResource):
    class Meta:
        model = Saidas
        ordering = ["nome"]


class SaidasAdmin(ImportExportModelAdmin):
    resource_class = SaidasResource
    list_display = ["nome"]
    #list_filter = ["nome"]

admin.site.register(Saidas, SaidasAdmin)


