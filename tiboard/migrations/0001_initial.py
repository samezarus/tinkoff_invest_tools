# Generated by Django 4.0 on 2021-12-19 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('add_dt', models.DateTimeField(default=datetime.datetime(2021, 12, 19, 5, 21, 12, 550853), verbose_name='Дата добавления')),
                ('update_dt', models.DateTimeField(default=datetime.datetime(2021, 12, 19, 5, 21, 12, 550865), verbose_name='Дата обновления')),
                ('update_flag', models.BooleanField(default=False, verbose_name='Признак обновления')),
                ('ti_figi', models.CharField(default='xxxxxxxxxxxxxxxxxxxx', max_length=20, primary_key=True, serialize=False, unique=True)),
                ('ti_ticker', models.CharField(max_length=20, verbose_name='ticker')),
                ('ti_isin', models.CharField(max_length=20, verbose_name='isin')),
                ('ti_min_price_increment', models.FloatField(default=0.1, verbose_name='Шаг цены')),
                ('ti_lot', models.IntegerField(default=1, verbose_name='Количество лотов')),
                ('ti_min_quantity', models.IntegerField(default=1, verbose_name='Минимальное количество')),
                ('ti_currency', models.CharField(max_length=7, verbose_name='Валюта')),
                ('ti_name', models.CharField(max_length=250, verbose_name='Название')),
                ('ti_type', models.CharField(max_length=10, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Инструмент',
                'verbose_name_plural': 'Инструменты',
            },
        ),
    ]