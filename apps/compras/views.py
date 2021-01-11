import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Compras
from .forms import ComprasForm
from apps.pecas.models import Pecas
from apps.estoque.models import Estoque


def ListaCompras(request):
    compras = Compras.objects.all().order_by("id")
    object = {"compras":compras}
    return render(request, 'compras/lista_compras.html', object)


def CriarCompras(request):
    if request.method == "POST":
        form = ComprasForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form = form.save(commit=False)
            id = form.item.id
            quantidade = form.quantidade
            pecas = get_object_or_404(Pecas, pk=id)
            form.unidade = pecas.unidade
            form.save()

            estoque = Estoque.objects.get(item_id=id)
            if estoque.quantidade == None:
                estoque.quantidade = 0
            estoque.quantidade += quantidade
            estoque.save()
            return redirect("lista_compras")

    else:
        form = ComprasForm(request.POST or None, request.FILES or None)
        object = {'form': form}

        return render(request, 'compras/criar_compras.html', object)


def DeletarCompras(request, id):
    compras = get_object_or_404(Compras, pk=id)

    if request.method == 'POST':
        id = compras.item.id
        quantidade = compras.quantidade
        estoque = Estoque.objects.get(item_id=id)
        estoque.quantidade -= quantidade
        estoque.save()
        compras.delete()
        return redirect('lista_compras')

    object = {'compras': compras}

    return render(request, 'compras/deletar_compras.html', object)


def EditarCompras(request, id):
    compras = get_object_or_404(Compras, pk=id)
    form = ComprasForm(request.POST or None, request.FILES or None, instance=compras)
    if compras.quantidade == None:
        compras.quantidade = 0
    quantidade_inicial = compras.quantidade
    if form.is_valid():
        id = compras.item.id
        quantidade = compras.quantidade
        form.save()

        estoque = Estoque.objects.get(item_id=id)
        if estoque.quantidade == None:
            estoque.quantidade = 0
        estoque.quantidade += quantidade - quantidade_inicial
        estoque.save()
        return redirect("lista_compras")


    object = {'form': form, 'compras': compras}
    return render(request, 'compras/editar_compras.html', object)









