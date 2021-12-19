from django.db import models
from datetime import datetime


class Instrument(models.Model):
    """
    Обязяательные поля:
        figi, ticker, lot, name, type

    Необязательные:
        isin, minPriceIncrement, minQuantity, currency
    """
    objects = models.Manager()

    add_dt = models.DateTimeField(verbose_name='Дата добавления', default=datetime.now())
    update_dt = models.DateTimeField(verbose_name='Дата обновления', default=datetime.now())
    update_flag = models.BooleanField(verbose_name='Признак обновления', default=False)

    ti_figi = models.CharField(primary_key=True, max_length=20, unique=True, default='xxxxxxxxxxxxxxxxxxxx')
    ti_ticker = models.CharField(verbose_name='ticker', max_length=20)
    ti_isin = models.CharField(verbose_name='isin', max_length=20)
    ti_min_price_increment = models.FloatField(verbose_name='Шаг цены', default=0.1)
    ti_lot = models.IntegerField(verbose_name='Количество лотов',  default=1)
    ti_min_quantity = models.IntegerField(verbose_name='Минимальное количество', default=1)
    ti_currency = models.CharField(verbose_name='Валюта', max_length=7)
    ti_name = models.CharField(verbose_name='Название', max_length=250)
    ti_type = models.CharField(verbose_name='Тип', max_length=10)

    def __str__(self):
        return self.ti_name

    class Meta:
        _base_word = 'Инструмент'
        verbose_name = f'{_base_word}'
        verbose_name_plural = f'{_base_word}ы'
