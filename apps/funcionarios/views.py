from django.shortcuts import render, get_object_or_404, redirect
from .models import Funcionarios
from .forms import FuncionariosForm

def ListaFuncionarios(request):
    funcionarios = Funcionarios.objects.all().order_by("id")
    object = {"funcionarios":funcionarios}
    return render(request, 'funcionarios/lista_funcionarios.html', object)


def CriarFuncionarios(request):
    if request.method == "POST":
        form = FuncionariosForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect("lista_funcionarios")

    else:
        form = FuncionariosForm(request.POST or None, request.FILES or None)
        object = {'form': form}

        return render(request, 'funcionarios/criar_funcionarios.html', object)


def DeletarFuncionarios(request, id):
    funcionarios = get_object_or_404(Funcionarios, pk=id)

    if request.method == 'POST':
        funcionarios.delete()
        return redirect('lista_funcionarios')

    object = {'funcionarios': funcionarios}

    return render(request, 'funcionarios/deletar_funcionarios.html', object)


def EditarFuncionarios(request, id):
    funcionarios = get_object_or_404(Funcionarios, pk=id)
    form = FuncionariosForm(request.POST or None, request.FILES or None, instance=funcionarios)
    if form.is_valid():
        form.save()
        return redirect("lista_funcionarios")

    object = {'form': form}

    return render(request, 'funcionarios/editar_funcionarios.html', object)










