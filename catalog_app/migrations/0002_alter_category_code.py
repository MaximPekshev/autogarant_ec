# Generated by Django 3.2.8 on 2022-12-27 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(blank=True, default='', max_length=36, null=True, verbose_name='Код'),
        ),
    ]
