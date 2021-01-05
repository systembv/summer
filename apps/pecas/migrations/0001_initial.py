# Generated by Django 3.1.4 on 2021-01-05 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pecas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Insira o item.', max_length=80, verbose_name='Item: ')),
                ('unidade', models.ForeignKey(blank=True, help_text='Insira a unidade', null=True, on_delete=django.db.models.deletion.PROTECT, to='unidades.unidade', verbose_name='Unidade: ')),
            ],
            options={
                'verbose_name': 'Peça',
                'verbose_name_plural': 'Peças',
            },
        ),
    ]
