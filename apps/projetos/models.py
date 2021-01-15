from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model
from apps.clientes.models import Clientes




class Projetos(models.Model):
    nome = models.CharField('Nome: ', max_length=80, help_text='Insira nome projeto')
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT, null=True, blank=True, help_text='Insira o cliente', verbose_name="Cliente:")



    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
