# Generated by Django 3.1.4 on 2021-01-07 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pecas', '0001_initial'),
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='item',
            field=models.ForeignKey(blank=True, help_text='Insira Item comprado', null=True, on_delete=django.db.models.deletion.PROTECT, to='pecas.pecas', verbose_name='Item comprado:'),
        ),
        migrations.AddField(
            model_name='compras',
            name='quantidade',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Insira quantidade comprada', max_digits=10, null=True, verbose_name='Quantidade comprada:'),
        ),
        migrations.AddField(
            model_name='compras',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Insira valor do item', max_digits=10, null=True, verbose_name='Valor do item:'),
        ),
    ]
