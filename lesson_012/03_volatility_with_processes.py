# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
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


import utils as ut
import multiprocessing
from itertools import islice
# from multiprocessing import Process, Pipe, Queue
from queue import Empty


PATH = 'trades'


class TickerInspector(multiprocessing.Process):

    def __init__(self, full_path, informator, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.full_path = full_path
        self.name_ticker = ''
        self.volatility = 0
        self.informator = informator   # определили очередь

    def run(self):
        prices = self.file_work()
        self.volatility_calculation(prices)
        # запихнули в очередь данные которые нам отдает класс
        # TODO на вход лучше передать словарь из двух ключей на значение им передать self.name_ticker,
        #  self.volatility_calculation
        self.informator.put(self.name_ticker, self.volatility_calculation)

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
    informator = multiprocessing.Queue()  # создали очередь
    calculator_volatilitys = [TickerInspector(file_name, informator) for file_name in ut.file_sniffer(PATH)]  # пердали ее в класс

    for calculator_volatility in calculator_volatilitys:
        calculator_volatility.start()
    # TODO join тормозит перенести за цикл while
    for calculator_volatility in calculator_volatilitys:
        calculator_volatility.join()

    while True:
        try:
            # TODO у нас не должно быть цикла
            # TODO мы тут получаем данные сразу из informator
            for calculator_volatility in calculator_volatilitys:
                name_ticker, volatility = calculator_volatility.informator.get()
                # name_ticker, volatility = calculator_volatility.name_ticker, calculator_volatility.volatility
                if volatility <= 0:
                    tickers_volatilitys_zero.append(name_ticker)
                else:
                    tickers_volatilitys[name_ticker] = volatility
        except Empty:
            # TODO тут должно быть условие проверки живы ли процессы если нет то выходим ждать нечего
            break  # если пусто просто выходим иои проверяем жив ли процесс?

    tickers_volatilitys_max, tickers_volatilitys_min = ut.filter_data(tickers_volatilitys)
    ut.print_result(tickers_volatilitys_max, tickers_volatilitys_min, tickers_volatilitys_zero)


if __name__ == '__main__':
    main()
