from django.urls import path, include
from . import views as v

urlpatterns = [
    path('', v.ListaProjetos, name= "lista_projetos"),
    path('criar/', v.CriarProjetos, name= "criar_projetos"),
    path('deletar/<int:id>/', v.DeletarProjetos, name= "deletar_projetos"),
    path('editar/<int:id>/', v.EditarProjetos, name= "editar_projetos"),
]
