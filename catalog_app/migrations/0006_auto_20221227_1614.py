# Generated by Django 3.2.8 on 2022-12-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0005_auto_20221227_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='art',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='good',
            name='code',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='good',
            name='okei',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Единица измерения'),
        ),
    ]
