# Generated by Django 3.1.4 on 2021-01-11 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_compras_unidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='nome',
            field=models.CharField(help_text='Insira nome', max_length=80, verbose_name='Nome: '),
        ),
    ]