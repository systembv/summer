from django.shortcuts import render, get_object_or_404, redirect


def ListaUnidades(request):
    object = {}
    return render(request, 'unidades/lista_unidades.html', object)
