# Generated by Django 3.1.4 on 2021-01-12 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
        ('saidas', '0004_saidas_unidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='saidas',
            name='responsavel',
            field=models.ForeignKey(blank=True, help_text='Funcionário responsável do pedido', null=True, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionarios', verbose_name='Responsável:'),
        ),
    ]
