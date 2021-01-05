from django.urls import path, include
from . import views as v

urlpatterns = [
    path('', v.ListaPecas, name= "lista_pecas"),
]
