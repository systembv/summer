from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
import json
from .models import Estoque
from .forms import EstoqueForm
from apps.compras.models import Compras


def ListaEstoques(request):
    estoques = Estoque.objects.all().order_by("id")

    qtd = 0
    for item in estoques:
        qtd += item.quantidade
    object = {"estoques": estoques, "qtd":qtd}

    return render(request, 'estoques/lista_estoques.html', object)


def EditarEstoques(request, id):
    estoque = get_object_or_404(Estoque, pk=id)
    form = EstoqueForm(request.POST or None, request.FILES or None, instance=estoque)
    if form.is_valid():
        estoque.valor_total = estoque.valor * estoque.quantidade
        form.save()
        return redirect("lista_estoques")

    object = {'form': form,}
    return render(request, 'estoques/editar_estoques.html', object)



def ComputarCompra(request, id):
    estoque = Estoque.objects.get(item_id=id)
    response = json.dumps({"mensagem": "Quantidade deste item no estoque é de " + str(estoque.quantidade) +' '+ str(estoque.unidade),
                           })

    return HttpResponse(response, content_type='application/json')