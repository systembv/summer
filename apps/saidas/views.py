from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Saidas
from .forms import SaidasForm
from apps.funcionarios.models import Funcionarios
from apps.pecas.models import Pecas
from apps.estoque.models import Estoque


def ListaSaidas(request):
    saidas = Saidas.objects.all().order_by("id")

    search = request.GET.get("pesquisa", None)

    if search:
        saidas = Saidas.objects.all().order_by("id")
        saidas = saidas.filter(item=search)

    else:
        saidas = Saidas.objects.all().order_by("id")
        paginator = Paginator(saidas, 3)
        page = request.GET.get("page")
        saidas = paginator.get_page(page)

    object = {"saidas":saidas}
    return render(request, 'saidas/lista_saidas.html', object)


def CriarSaidas(request):
    if request.method == "POST":
        form = SaidasForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            id = request.user.id
            form = form.save(commit=False)
            form.responsavel = Funcionarios.objects.get(user_id=id)
            item_id = form.item.id
            quantidade = form.quantidade
            if quantidade == None:
                quantidade = 0
            pecas = get_object_or_404(Pecas, pk=item_id)
            form.unidade = pecas.unidade
            form.save()

            estoque = Estoque.objects.get(item_id=item_id)
            if estoque.quantidade == None:
                estoque.quantidade = 0
            estoque.quantidade -= quantidade
            estoque.save()

            return redirect("lista_saidas")

    else:
        form = SaidasForm(request.POST or None, request.FILES or None)
        object = {'form': form}

        return render(request, 'saidas/criar_saidas.html', object)


def DeletarSaidas(request, id):
    saidas = get_object_or_404(Saidas, pk=id)

    if request.method == 'POST':
        id = saidas.item.id
        quantidade = saidas.quantidade
        estoque = Estoque.objects.get(item_id=id)
        estoque.quantidade += quantidade
        estoque.save()
        saidas.delete()
        return redirect('lista_saidas')

    object = {'saidas': saidas}

    return render(request, 'saidas/deletar_saidas.html', object)


def EditarSaidas(request, id):
    saidas = get_object_or_404(Saidas, pk=id)
    form = SaidasForm(request.POST or None, request.FILES or None, instance=saidas)
    unidade_saida = saidas.unidade
    responsavel_saida = saidas.responsavel
    if saidas.quantidade == None:
        saidas.quantidade = 0
    quantidade_inicial = saidas.quantidade
    if form.is_valid():
        print(unidade_saida)
        id = saidas.item.id
        saidas.unidade = unidade_saida
        saidas.responsavel = responsavel_saida
        quantidade = saidas.quantidade
        form.save()

        estoque = Estoque.objects.get(item_id=id)
        if estoque.quantidade == None:
            estoque.quantidade = 0
        estoque.quantidade -= quantidade - quantidade_inicial
        estoque.save()
        return redirect("lista_saidas")

    object = {'form': form}

    return render(request, 'saidas/editar_saidas.html', object)










