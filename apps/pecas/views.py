from django.shortcuts import render, get_object_or_404, redirect
from .models import Pecas
from .forms import PecasForm

def ListaPecas(request):
    pecas = Pecas.objects.all().order_by("id")
    object = {"pecas":pecas}
    return render(request, 'pecas/lista_pecas.html', object)


def CriarPecas(request):
    if request.method == "POST":
        form = PecasForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
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
        return redirect("lista_pecas")

    object = {'form': form}

    return render(request, 'pecas/editar_pecas.html', object)










