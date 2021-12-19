"""
Модуль для получения данных с электросчётчиков на данное время
"""

from django.core.management.base import BaseCommand  # (1)


import os
APP_DIR = os.path.dirname(os.path.realpath(__file__))
LOGS_DIR = f"{APP_DIR}/logs"

import sys
# sys.path.append(os.getenv('PROJECT_DIR'))
# print('----------------------------')
# for item in sys.path:
#     print(item)
# print('----------------------------')


from django.conf import settings
#from django.db import models
from tiboard.models import *


from _core.tinkoff_invest.ti_core import TinkoffInvest


import logging
from datetime import datetime






if not os.path.isdir(LOGS_DIR):
    os.makedirs(LOGS_DIR)


# Конфигурация модуля логов
logger = logging.getLogger('update_instruments.py')
logger.setLevel(logging.INFO)
fh = logging.FileHandler(filename=f'{LOGS_DIR}/{datetime.now().date()}.log', encoding='UTF-8')
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] [%(message)s]')
fh.setFormatter(formatter)
logger.addHandler(fh)


class Command(BaseCommand):
    help = 'Обновление списка инструментов'

    def handle(self, *args, **options):


        tinvest = TinkoffInvest()

        stocks = tinvest.get_market_stocks()

        for stock in stocks:
            # Получаем обязательные параметры
            ti_figi = stock['figi']
            ti_ticker = stock['ticker']
            ti_lot = stock['lot']
            ti_name = stock['name']
            ti_type = stock['type']

            # Получаем необязательные параметры
            ti_isin = ''
            ti_min_price_increment = 1.0
            ti_min_quantity = 1
            ti_currency = ''

            key = 'isin'
            if key in stock:
                ti_isin = stock[key]

            key = 'minPriceIncrement'
            if key in stock:
                ti_min_price_increment = stock[key]

            key = 'minQuantity'
            if key in stock:
                ti_min_quantity = stock[key]

            key = 'currency'
            if key in stock:
                ti_currency = stock[key]

            # Пытаемся записать инструмент в ORM
            Instrument.objects.update_or_create(
                ti_figi=ti_figi,
                ti_ticker=ti_ticker,
                ti_lot=ti_lot,
                ti_name=ti_name,
                ti_type=ti_type,
                ti_isin=ti_isin,
                ti_min_price_increment=ti_min_price_increment,
                ti_min_quantity=ti_min_quantity,
                ti_currency=ti_currency
            )
