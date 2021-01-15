from django.shortcuts import render, get_object_or_404, redirect
from .models import Projetos
from .forms import ProjetosForm


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
    object = {"projetos":projetos}
    return render(request, 'projetos/detalhes_projeto.html', object)







