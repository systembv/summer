from django.shortcuts import render, get_object_or_404, redirect
from .models import Pecas
from .forms import PecasForm
from apps.estoque.models import Estoque
from apps.unidades.models import Unidade
from apps.estoque.models import Estoque
from apps.compras.models import Compras
from apps.saidas.models import Saidas


def ListaPecas(request):
    pecas = Pecas.objects.all().order_by("id")
    object = {"pecas":pecas}
    return render(request, 'pecas/lista_pecas.html', object)


def CriarPecas(request):
    if request.method == "POST":
        form = PecasForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form_pecas = form.save(commit=False)
            form_pecas.save()

            id = form_pecas.id
            unidade = form_pecas.unidade.id
            estoque = Estoque()
            estoque.item = Pecas.objects.get(pk=id)
            estoque.unidade = Unidade.objects.get(pk=unidade)
            estoque.save()

            return redirect("lista_pecas")

    else:
        form = PecasForm(request.POST or None, request.FILES or None)
        object = {'form': form}

        return render(request, 'pecas/criar_pecas.html', object)


def DeletarPecas(request, id):
    pecas = get_object_or_404(Pecas, pk=id)

    if request.method == 'POST':
        pecas.delete()
        return redirect('lista_pecas')

    object = {'pecas': pecas}

    return render(request, 'pecas/deletar_pecas.html', object)


def EditarPecas(request, id):
    pecas = get_object_or_404(Pecas, pk=id)
    form = PecasForm(request.POST or None, request.FILES or None, instance=pecas)
    if form.is_valid():
        form.save()

        pecas = Pecas.objects.get(id=id)
        pecas_id = id
        unidade=pecas.unidade
        try:
            estoque = Estoque.objects.get(item_id=id)
            estoque.unidade = unidade
            estoque.save()
        except:
            estoque = Estoque()
            estoque.item = Pecas.objects.get(pk=id)
            estoque.unidade = Unidade.objects.get(pk=unidade.id)
            estoque.save()


        for item in Compras.objects.all():
            if item.item.id == pecas_id:
                item.unidade = unidade
                item.save()

        for item in Saidas.objects.all():
            if item.item.id == pecas_id:
                item.unidade = unidade
                item.save()




        return redirect("lista_pecas")

    object = {'form': form}

    return render(request, 'pecas/editar_pecas.html', object)










