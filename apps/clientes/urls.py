from django.urls import path, include
from . import views as v

urlpatterns = [
    path('', v.ListaClientes, name= "lista_clientes"),
    path('criar/', v.CriarClientes, name= "criar_clientes"),
    path('deletar/<int:id>/', v.DeletarClientes, name= "deletar_clientes"),
    path('editar/<int:id>/', v.EditarClientes, name= "editar_clientes"),
]
