# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от полусуммы крайних значений цены за торговую сессию:
#   полусумма = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / полусумма) * 100%
# Например для бумаги №1:
#   half_sum = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / half_sum) * 100 = 8.7%
# Для бумаги №2:
#   half_sum = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / half_sum) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

import os
from itertools import islice


PATH = 'trades'


class TickerInspector:

    def __init__(self, path):
        self.path = path
        self.files_trades = []
        self.tickers_volatility = {}
        self.tickers_volatility_max = {}
        self.tickers_volatility_min = {}
        self.tickers_volatility_zero = {}

    def run(self):
        prices = []
        self.file_sniffer()
        for file in self.files_trades:
            file = os.path.join(self.path, file)
            with open(file, 'r', encoding='utf-8') as file_read:
                for line in islice(file_read, 1, None):
                    secid, _, price, _ = line.split(',')
                    prices.append(price)
                prices = list(map(float, prices))
                half_sum = (max(prices) + min(prices)) / 2
                volatility = ((max(prices) - min(prices)) / half_sum) * 100
                if volatility <= 0:
                    self.tickers_volatility_zero[secid] = round(volatility, 2)
                else:
                    self.tickers_volatility[secid] = round(volatility, 2)
                prices = []
        self.filter_volatility()
        self.print_result()

    def file_sniffer(self):
        self.files_trades = os.listdir(self.path)

    def filter_volatility(self):
        self.tickers_volatility = dict(sorted(self.tickers_volatility.items(), key=lambda element: element[1],
                                              reverse=True))
        # TODO есть ли способы уменьшить код?
        for item in range(0, 3):
            self.tickers_volatility_max[list(self.tickers_volatility.keys())[item]] = list(
                self.tickers_volatility.values())[item]
        for item in range(len(self.tickers_volatility)-1, len(self.tickers_volatility)-4, -1):
            self.tickers_volatility_min[list(self.tickers_volatility.keys())[item]] = list(
                self.tickers_volatility.values())[item]

    def print_result(self):
        print(f'Максимальная волатильность:')
        for key, value in self.tickers_volatility_max.items():
            print(f'ТИКЕР {key} - {value}%')
        print(f'Минимальная волатильность:')
        for key, value in self.tickers_volatility_min.items():
            print(f'ТИКЕР {key} - {value}%')
        print(f'Нулевая волатильность:')
        for key in self.tickers_volatility_zero.keys():
            print(f'{key}', end=', ')  # TODO прошу подсказать как тут поставить . после последнего значения?


ticker = TickerInspector(PATH)
ticker.run()
