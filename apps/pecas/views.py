from django.shortcuts import render, get_object_or_404, redirect


def ListaPecas(request):
    object = {}
    return render(request, 'pecas/lista_pecas.html', object)
