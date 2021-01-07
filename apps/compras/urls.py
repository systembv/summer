from django.urls import path, include
from . import views as v

urlpatterns = [
    path('', v.ListaCompras, name= "lista_compras"),
    path('criar/', v.CriarCompras, name= "criar_compras"),
    path('deletar/<int:id>/', v.DeletarCompras, name= "deletar_compras"),
    path('editar/<int:id>/', v.EditarCompras, name= "editar_compras"),
]
