from django.forms import ModelForm
from django import forms
from .models import Unidade
from django.core import validators


class UnidadeForm(ModelForm):

    class Meta:
        model = Unidade
        fields = (
                "nome",
                )

        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite...'}),
        }


