from django.shortcuts import render, get_object_or_404, redirect
from .models import Clientes
from .forms import ClientesForm

def ListaClientes(request):
    clientes = Clientes.objects.all().order_by("id")
    object = {"clientes":clientes}
    return render(request, 'clientes/lista_clientes.html', object)


def CriarClientes(request):
    if request.method == "POST":
        form = ClientesForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect("lista_clientes")

    else:
        form =ClientesForm(request.POST or None, request.FILES or None)
        object = {'form': form}

        return render(request, 'clientes/criar_clientes.html', object)


def DeletarClientes(request, id):
    clientes = get_object_or_404(Clientes, pk=id)

    if request.method == 'POST':
        clientes.delete()
        return redirect('lista_clientes')

    object = {'clientes': clientes}

    return render(request, 'clientes/deletar_clientes.html', object)


def EditarClientes(request, id):
    clientes = get_object_or_404(Clientes, pk=id)
    form = ClientesForm(request.POST or None, request.FILES or None, instance=clientes)
    if form.is_valid():
        form.save()
        return redirect("lista_clientes")

    object = {'form': form}

    return render(request, 'clientes/editar_clientes.html', object)










