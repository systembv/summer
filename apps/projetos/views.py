from django.shortcuts import render, get_object_or_404, redirect
from .models import Projetos
from .forms import ProjetosForm
from apps.saidas.models import Saidas
from apps.estoque.models import Estoque

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


    val_total = []
    for item in saidas:
        id = item.item.id
        peca = Estoque.objects.get(item_id=id)
        val_total.append(item.quantidade * peca.valor)

    valor_pecas = 0
    for val in val_total:
        valor_pecas += val

    valor_pecas = "{:,.2f}".format(valor_pecas).replace(".","..").replace(",",".").replace("..",",")


    ziplist = zip(saidas, val_total)

    object = {"projetos":projetos, "saidas":saidas,
              "valor":valor_pecas, "val_item":val_total, "ziplist":ziplist}
    return render(request, 'projetos/detalhes_projeto.html', object)







