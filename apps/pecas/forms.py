from django.forms import ModelForm
from django import forms
from .models import Pecas
from django.core import validators


class PecasForm(ModelForm):

    class Meta:
        model = Pecas
        fields = (
                "nome",
                "unidade",
                )

        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite...'}),
            "unidade": forms.Select(attrs={'class': 'form-select'}),
        }


