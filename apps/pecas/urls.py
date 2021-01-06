from django.urls import path, include
from . import views as v

urlpatterns = [
    path('', v.ListaPecas, name= "lista_pecas"),
    path('criar/', v.CriarPecas, name= "criar_pecas"),
    path('deletar/<int:id>/', v.DeletarPecas, name= "deletar_pecas"),
    path('editar/<int:id>/', v.EditarPecas, name= "editar_pecas"),
]
