from django.forms import ModelForm
from django import forms
from .models import Estoque
from django.core import validators


class EstoqueForm(ModelForm):

    class Meta:
        model = Estoque
        fields = (
                "item", "unidade", "quantidade",
                )




