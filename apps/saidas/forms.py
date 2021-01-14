from django.forms import ModelForm
from django import forms
from .models import Saidas
from django.core import validators


class SaidasForm(ModelForm):

    class Meta:
        model = Saidas
        fields = (
                "nome", "item", "quantidade", "unidade", "responsavel"
                )

        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite...'}),
        }


