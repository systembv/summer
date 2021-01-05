from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model



class Unidade(models.Model):
    nome = models.CharField('Denominação: ', max_length=80, help_text='Insira tipo da unidade.')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
