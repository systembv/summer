from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



class Funcionarios(models.Model):
    nome = models.CharField('Nome: ', max_length=80, help_text='Insira nome do funcionário')
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
