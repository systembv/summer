# Generated by Django 3.1.4 on 2021-01-27 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saidas', '0006_saidas_projeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='saidas',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Valor item saida', max_digits=10, null=True, verbose_name='Valor:'),
        ),
        migrations.AddField(
            model_name='saidas',
            name='valor_total',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Valor total saida', max_digits=10, null=True, verbose_name='Valor total:'),
        ),
    ]
