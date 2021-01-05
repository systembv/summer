from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model
from apps.unidades.models import Unidade


class Pecas(models.Model):
    nome = models.CharField('Item: ', max_length=80, help_text='Insira o item.')
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, null=True, blank=True,
                                    help_text='Insira a unidade', verbose_name="Unidade: ")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Peça'
        verbose_name_plural = 'Peças'
