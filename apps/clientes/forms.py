from django.forms import ModelForm
from django import forms
from .models import Clientes
from django.core import validators


class ClientesForm(ModelForm):

    class Meta:
        model = Clientes
        fields = (
                "nome",
                )

        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite...'}),
        }


