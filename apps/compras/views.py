from django.shortcuts import render, get_object_or_404, redirect
from .models import Compras
from .forms import ComprasForm


def ListaCompras(request):
    compras = Compras.objects.all().order_by("id")
    object = {"compras":compras}
    return render(request, 'compras/lista_compras.html', object)


def CriarCompras(request):
    if request.method == "POST":
        form = ComprasForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect("lista_compras")

    else:
        form = ComprasForm(request.POST or None, request.FILES or None)
        object = {'form': form}

        return render(request, 'compras/criar_compras.html', object)


def DeletarCompras(request, id):
    compras = get_object_or_404(Compras, pk=id)

    if request.method == 'POST':
        compras.delete()
        return redirect('lista_compras')

    object = {'compras': compras}

    return render(request, 'compras/deletar_compras.html', object)


def EditarCompras(request, id):
    compras = get_object_or_404(Compras, pk=id)
    form = ComprasForm(request.POST or None, request.FILES or None, instance=compras)
    if form.is_valid():
        form.save()
        return redirect("lista_compras")

    object = {'form': form}

    return render(request, 'compras/editar_compras.html', object)










