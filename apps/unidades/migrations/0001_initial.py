# Generated by Django 3.1.4 on 2021-01-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Insira tipo da unidade.', max_length=80, verbose_name='Denominação: ')),
            ],
            options={
                'verbose_name': 'Unidade',
                'verbose_name_plural': 'Unidades',
            },
        ),
    ]
