# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
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
#
# Внимание! это задание можно выполнять только после зачета lesson_012/01_volatility.py !!!

# тут ваш код в многопоточном стиле


import utils as ut
from itertools import islice
from threading import Thread


PATH = 'trades'


class TickerInspector(Thread):

    def __init__(self, full_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.full_path = full_path
        self.name_ticker = ''
        self.volatility = 0

    def run(self):
        prices = self.file_work()
        self.volatility_calculation(prices)

    def file_work(self):
        tickers_prices = []
        with open(self.full_path, 'r', encoding='utf-8') as file_read:
            print(f'открыли файл {self.full_path}', flush=True)
            for line in islice(file_read, 1, None):
                name_ticker, _, price, _ = line.split(',')
                tickers_prices.append(float(price))
            self.name_ticker = name_ticker
        print(f'закрыли файл {self.full_path}', flush=True)
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
        calculator_volatility.start()
    for calculator_volatility in calculator_volatilitys:
        calculator_volatility.join()

    for calculator_volatility in calculator_volatilitys:
        name_ticker, volatility = calculator_volatility.name_ticker, calculator_volatility.volatility
        if volatility <= 0:
            tickers_volatilitys_zero.append(name_ticker)
        else:
            tickers_volatilitys[name_ticker] = volatility

    tickers_volatilitys_max, tickers_volatilitys_min = ut.filter_data(tickers_volatilitys)
    ut.print_result(tickers_volatilitys_max, tickers_volatilitys_min, tickers_volatilitys_zero)

# TODO странно но при работе в потоках время увеличивается.
if __name__ == '__main__':
    main()
