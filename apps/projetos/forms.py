from django.forms import ModelForm
from django import forms
from .models import Projetos
from django.core import validators


class ProjetosForm(ModelForm):

    class Meta:
        model = Projetos
        fields = (
                "nome", "cliente"
                )

        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite...'}),
        }


