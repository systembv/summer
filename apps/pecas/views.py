from django.shortcuts import render, get_object_or_404, redirect
from .models import Pecas
from .forms import PecasForm

def ListaPecas(request):
    pecas = Pecas.objects.all().order_by("id")
    object = {"pecas":pecas}
    return render(request, 'pecas/lista_pecas.html', object)
