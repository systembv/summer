from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    object = {}
    return render(request, 'core/home.html', object)
