from django.shortcuts import render, get_object_or_404, redirect
from .models import Projetos
from .forms import ProjetosForm
from apps.saidas.models import Saidas

def ListaProjetos(request):
    projetos = Projetos.objects.all().order_by("id")
    object = {"projetos":projetos}
    return render(request, 'projetos/lista_projetos.html', object)


def CriarProjetos(request):
    if request.method == "POST":
        form = ProjetosForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect("lista_projetos")

    else:
        form = ProjetosForm(request.POST or None, request.FILES or None)
        object = {'form': form}

        return render(request, 'projetos/criar_projetos.html', object)


def DeletarProjetos(request, id):
    projetos = get_object_or_404(Projetos, pk=id)

    if request.method == 'POST':
        projetos.delete()
        return redirect('lista_unidades')

    object = {'projetos': projetos}

    return render(request, 'projetos/deletar_projetos.html', object)


def EditarProjetos(request, id):
    projetos = get_object_or_404(Projetos, pk=id)
    form = ProjetosForm(request.POST or None, request.FILES or None, instance=projetos)
    if form.is_valid():
        form.save()
        return redirect("lista_projetos")

    object = {'form': form}

    return render(request, 'projetos/editar_projetos.html', object)


def DetalhesProjeto(request, id):
    projetos = Projetos.objects.all().filter(id=id)
    saidas = Saidas.objects.all().filter(projeto_id=id)

    quantidade_pecas = 0
    for item in saidas:
        if item.quantidade == None:
            item.quantidade = 0,00
        quantidade_pecas += item.quantidade

    object = {"projetos":projetos, "saidas":saidas, "quantidade":quantidade_pecas}
    return render(request, 'projetos/detalhes_projeto.html', object)







