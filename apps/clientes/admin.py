from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Clientes
from import_export import resources



class ClientesResource(resources.ModelResource):
    class Meta:
        model = Clientes
        ordering = ["nome"]


class ClientesAdmin(ImportExportModelAdmin):
    resource_class = ClientesResource
    list_display = ["nome"]
    #list_filter = ["nome"]

admin.site.register(Clientes, ClientesAdmin)

