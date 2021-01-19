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
            valor = form.valor
            valor_total = quantidade * valor
            pecas = get_object_or_404(Pecas, pk=id)
            form.unidade = pecas.unidade
            form.save()

            estoque = Estoque.objects.get(item_id=id)
            valor_estoque_ini = estoque.valor_total
            quantidade_estoque_ini = estoque.quantidade
            estoque.quantidade += quantidade
            estoque.valor_total += valor_total
            estoque.valor = (valor_total + valor_estoque_ini) / (quantidade_estoque_ini + quantidade )
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
        valor = compras.valor
        valor_total = quantidade * valor
        estoque = Estoque.objects.get(item_id=id)
        if estoque.valor_total - valor_total == 0:
            estoque.valor = 0
        else:
            estoque.valor = (estoque.valor_total - valor_total) / (estoque.quantidade - quantidade)
        estoque.quantidade -= quantidade
        estoque.valor_total -= valor_total
        estoque.save()
        compras.delete()
        return redirect('lista_compras')

    object = {'compras': compras}

    return render(request, 'compras/deletar_compras.html', object)


def EditarCompras(request, id):
    compras = get_object_or_404(Compras, pk=id)
    form = ComprasForm(request.POST or None, request.FILES or None, instance=compras)
    quantidade_inicial = compras.quantidade
    valor_inicial = compras.valor
    valor_total_inicial = quantidade_inicial * valor_inicial
    id = compras.item.id
    if form.is_valid():
        quantidade_nova = compras.quantidade
        valor_novo = compras.valor
        valor_total_novo = quantidade_nova * valor_novo
        estoque = Estoque.objects.get(item_id=id)
        quantidade_saldo = quantidade_nova - quantidade_inicial
        valor_total_saldo = valor_total_novo - valor_total_inicial
        estoque.valor = (estoque.valor_total + valor_total_saldo) / (estoque.quantidade + quantidade_saldo)
        estoque.quantidade += quantidade_saldo
        estoque.valor_total = estoque.valor * estoque.quantidade
        form.save()
        estoque.save()
        return redirect("lista_compras")

    object = {'form': form, 'compras': compras}
    return render(request, 'compras/editar_compras.html', object)









