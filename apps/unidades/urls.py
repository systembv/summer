from django.urls import path, include
from . import views as v

urlpatterns = [
    path('', v.ListaUnidades, name= "lista_unidades"),
    path('criar/', v.CriarUnidades, name= "criar_unidades"),
    path('deletar/<int:id>/', v.DeletarUnidades, name= "deletar_unidades"),
    path('editar/<int:id>/', v.EditarUnidades, name= "editar_unidades"),
]
