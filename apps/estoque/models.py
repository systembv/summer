from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model
from apps.pecas.models import Pecas
from apps.unidades.models import Unidade

class Estoque(models.Model):
    item = models.ForeignKey(Pecas, on_delete=models.PROTECT, verbose_name="Itens:")
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, verbose_name="Unidade:")
    quantidade = models.DecimalField('Quantidade do item:', max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.item)

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'
