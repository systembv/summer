from django.urls import path, include
from . import views as v
from .views import (ComputarCompra,
                    )


urlpatterns = [
    path('', v.ListaEstoques, name= "lista_estoques"),
    path('editar/<int:id>/', v.EditarEstoques, name= "editar_estoques"),
    #path('computar_compra/<int:id>/', ComputarCompra.as_view(), name= "computar_compra"),
    path('computar_compra/<int:id>/', v.ComputarCompra, name="computar_compra"),

]
