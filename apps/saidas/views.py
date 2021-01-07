from django.shortcuts import render, get_object_or_404, redirect
from .models import Saidas
from .forms import SaidasForm


def ListaSaidas(request):
    saidas = Saidas.objects.all().order_by("id")
    object = {"saidas":saidas}
    return render(request, 'saidas/lista_saidas.html', object)


def CriarSaidas(request):
    if request.method == "POST":
        form = SaidasForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect("lista_saidas")

    else:
        form = SaidasForm(request.POST or None, request.FILES or None)
        object = {'form': form}

        return render(request, 'saidas/criar_saidas.html', object)


def DeletarSaidas(request, id):
    saidas = get_object_or_404(Saidas, pk=id)

    if request.method == 'POST':
        saidas.delete()
        return redirect('lista_saidas')

    object = {'saidas': saidas}

    return render(request, 'saidas/deletar_saidas.html', object)


def EditarSaidas(request, id):
    saidas = get_object_or_404(Saidas, pk=id)
    form = SaidasForm(request.POST or None, request.FILES or None, instance=saidas)
    if form.is_valid():
        form.save()
        return redirect("lista_saidas")

    object = {'form': form}

    return render(request, 'saidas/editar_saidas.html', object)










