from django.urls import path, include
from . import views as v

urlpatterns = [
    path('', v.ListaUnidades, name= "lista_unidades"),
]
