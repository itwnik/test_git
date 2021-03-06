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

import utils as ut
from itertools import islice


PATH = 'trades'


class TickerInspector:

    def __init__(self, full_path):
        self.full_path = full_path
        self.name_ticker = ''
        self.volatility = 0

    def run(self):
        prices = self.file_work()
        self.volatility_calculation(prices)

    def file_work(self):
        tickers_prices = []
        with open(self.full_path, 'r', encoding='utf-8') as file_read:
            for line in islice(file_read, 1, None):
                name_ticker, _, price, _ = line.split(',')
                tickers_prices.append(float(price))
            self.name_ticker = name_ticker
        return tickers_prices

    def volatility_calculation(self, prices):
        half_sum = (max(prices) + min(prices)) / 2
        self.volatility = round(((max(prices) - min(prices)) / half_sum) * 100, 2)


@ut.time_track
def main():
    tickers_volatilitys = {}
    tickers_volatilitys_zero = []
    calculator_volatilitys = [TickerInspector(file_name) for file_name in ut.file_sniffer(PATH)]

    for calculator_volatility in calculator_volatilitys:
        calculator_volatility.run()

    for calculator_volatility in calculator_volatilitys:
        name_ticker, volatility = calculator_volatility.name_ticker, calculator_volatility.volatility
        # этим условием тут мы избавились от лишнего цикла, увеличив скорость
        if volatility <= 0:  # странно, мне казалось, удобнее когдда все списки в одном месте формируются. не так?
            tickers_volatilitys_zero.append(name_ticker)
        else:
            tickers_volatilitys[name_ticker] = volatility

    tickers_volatilitys_max, tickers_volatilitys_min = ut.filter_data(tickers_volatilitys)
    ut.print_result(tickers_volatilitys_max, tickers_volatilitys_min, tickers_volatilitys_zero)


#  напишите ваши спеки частоту процессора ядерность и время сколько работала функция
#  до и после улучшений
#   Intel(R)_Core(TM)_i5-8265U_CPU_@_1.60GHz (8 ядер)
#   непонятно, до каких улучшений. Первый раз когда я замерял, программа работала 4,5 сек. Сейчас она работает 2,4 сек
if __name__ == '__main__':
    main()

# зачет!
