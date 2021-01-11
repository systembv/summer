from django.urls import path, include
from . import views as v

urlpatterns = [
    path('', v.ListaFuncionarios, name= "lista_funcionarios"),
    path('criar/', v.CriarFuncionarios, name= "criar_funcionarios"),
    path('deletar/<int:id>/', v.DeletarFuncionarios, name= "deletar_funcionarios"),
    path('editar/<int:id>/', v.EditarFuncionarios, name= "editar_funcionarios"),
]
