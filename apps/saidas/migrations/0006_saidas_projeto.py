# Generated by Django 3.1.4 on 2021-01-14 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
        ('saidas', '0005_saidas_responsavel'),
    ]

    operations = [
        migrations.AddField(
            model_name='saidas',
            name='projeto',
            field=models.ForeignKey(blank=True, help_text='Insira projeto para o item', null=True, on_delete=django.db.models.deletion.PROTECT, to='projetos.projetos', verbose_name='Projeto:'),
        ),
    ]
