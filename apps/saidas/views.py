from django.shortcuts import render, get_object_or_404, redirect


def ListaSaidas(request):
    object = {}
    return render(request, 'saidas/lista_saidas.html', object)
