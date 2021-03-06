from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model



class Clientes(models.Model):
    nome = models.CharField('Nome: ', max_length=80, help_text='Insira nome do cliente.')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
