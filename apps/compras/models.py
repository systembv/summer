from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model
from apps.pecas.models import Pecas
from apps.unidades.models import Unidade



class Compras(models.Model):
    nome = models.CharField('Nome: ', max_length=80, help_text='Insira nome')
    item = models.ForeignKey(Pecas, on_delete=models.PROTECT, null=True, blank=True,
                             help_text='Insira Item comprado', verbose_name="Item comprado:")
    quantidade = models.DecimalField('Quantidade comprada:', max_digits=10, decimal_places=2, blank=True, null=True,
                                     help_text='Insira quantidade comprada')
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, null=True, blank=True, help_text='Insira a unidade', verbose_name="Unidade:")
    valor = models.DecimalField('Valor do item:', max_digits=10, decimal_places=2, blank=True, null=True,
                                help_text='Insira valor do item')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
