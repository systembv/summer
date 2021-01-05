from django.shortcuts import render, get_object_or_404, redirect


def ListaCompras(request):
    object = {}
    return render(request, 'compras/lista_compras.html', object)
