# Generated by Django 3.1.4 on 2021-01-07 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unidades', '0001_initial'),
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='quantidade',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Quantidade do item:'),
        ),
        migrations.AddField(
            model_name='estoque',
            name='unidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='unidades.unidade', verbose_name='Unidade:'),
            preserve_default=False,
        ),
    ]