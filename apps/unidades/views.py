from django.shortcuts import render, get_object_or_404, redirect
from .models import Unidade
from .forms import UnidadeForm

def ListaUnidades(request):
    unidades = Unidade.objects.all().order_by("id")
    object = {"unidades":unidades}
    return render(request, 'unidades/lista_unidades.html', object)


def CriarUnidades(request):
    if request.method == "POST":
        form = UnidadeForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect("lista_unidades")

    else:
        form = UnidadeForm(request.POST or None, request.FILES or None)
        object = {'form': form}

        return render(request, 'unidades/criar_unidades.html', object)


def DeletarUnidades(request, id):
    unidades = get_object_or_404(Unidade, pk=id)

    if request.method == 'POST':
        unidades.delete()
        return redirect('lista_unidades')

    object = {'unidades': unidades}

    return render(request, 'unidades/deletar_unidades.html', object)


def EditarUnidades(request, id):
    unidades = get_object_or_404(Unidade, pk=id)
    form = UnidadeForm(request.POST or None, request.FILES or None, instance=unidades)
    if form.is_valid():
        form.save()
        return redirect("lista_unidades")

    object = {'form': form}

    return render(request, 'unidades/editar_unidades.html', object)










