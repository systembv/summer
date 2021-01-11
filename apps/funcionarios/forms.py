from django.forms import ModelForm
from django import forms
from .models import Funcionarios
from django.core import validators


class FuncionariosForm(ModelForm):

    class Meta:
        model = Funcionarios
        fields = (
                "nome",
                )

        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite...'}),
        }


