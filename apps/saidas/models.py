from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model
from apps.pecas.models import Pecas
from apps.unidades.models import Unidade
from apps.funcionarios.models import Funcionarios
from apps.projetos.models import Projetos


class Saidas(models.Model):
    nome = models.CharField('Item de saida: ', max_length=80, help_text='Insira item de saida')
    responsavel = models.ForeignKey(Funcionarios, on_delete=models.PROTECT, null=True, blank=True, help_text='Funcionário responsável do pedido', verbose_name="Responsável:")
    item = models.ForeignKey(Pecas, on_delete=models.PROTECT, null=True, blank=True, help_text='Insira o item de saida', verbose_name="Item de saida:")
    quantidade = models.DecimalField('Quantidade:', max_digits=10, decimal_places=2, blank=True, null=True, help_text='Quantidade item saida')
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, null=True, blank=True, help_text='Insira a unidade', verbose_name="Unidade:")
    projeto = models.ForeignKey(Projetos, on_delete=models.PROTECT, null=True, blank=True, help_text='Insira projeto para o item', verbose_name="Projeto:")


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Saida'
        verbose_name_plural = 'Saidas'
