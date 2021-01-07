# Generated by Django 3.1.4 on 2021-01-07 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saidas', '0002_auto_20210107_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saidas',
            name='quantidade',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Quantidade item saida', max_digits=10, null=True, verbose_name='Quantidade:'),
        ),
    ]
