# Generated by Django 3.2.8 on 2022-12-27 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0007_price_pricetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.SlugField(max_length=36, unique=True, verbose_name='Идентификатор')),
                ('code', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Код')),
                ('name', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склады',
            },
        ),
        migrations.CreateModel(
            name='StockBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.SmallIntegerField(blank=True, default=0, null=True, verbose_name='Остаток')),
                ('reserve', models.SmallIntegerField(blank=True, default=0, null=True, verbose_name='Резерв')),
                ('free', models.SmallIntegerField(blank=True, default=0, null=True, verbose_name='Свободный остаток')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_app.division', verbose_name='Склад')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_app.good', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Цена товара',
                'verbose_name_plural': 'Цены товаров',
                'unique_together': {('good', 'division')},
            },
        ),
    ]
