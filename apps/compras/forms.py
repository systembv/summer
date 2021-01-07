from django.forms import ModelForm
from django import forms
from .models import Compras
from django.core import validators


class ComprasForm(ModelForm):

    class Meta:
        model = Compras
        fields = (
                "nome", "item", "quantidade", "valor", "unidade"
                )

        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite...'}),
        }


