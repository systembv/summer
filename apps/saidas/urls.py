from django.urls import path, include
from . import views as v

urlpatterns = [
    path('', v.ListaSaidas, name= "lista_saidas"),
    path('criar/', v.CriarSaidas, name= "criar_saidas"),
    path('deletar/<int:id>/', v.DeletarSaidas, name= "deletar_saidas"),
    path('editar/<int:id>/', v.EditarSaidas, name= "editar_saidas"),
]
