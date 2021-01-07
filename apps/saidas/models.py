from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model
from apps.pecas.models import Pecas
from apps.unidades.models import Unidade


class Saidas(models.Model):
    nome = models.CharField('Item de saida: ', max_length=80, help_text='Insira item de saida')
    item = models.ForeignKey(Pecas, on_delete=models.PROTECT, null=True, blank=True, help_text='Insira o item de saida', verbose_name="Item de saida:")
    quantidade = models.DecimalField('Quantidade:', max_digits=10, decimal_places=2, blank=True, null=True, help_text='Quantidade item saida')
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, null=True, blank=True, help_text='Insira a unidade', verbose_name="Unidade:")


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Saida'
        verbose_name_plural = 'Saidas'
