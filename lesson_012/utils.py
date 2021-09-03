import os
import time


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate


def file_sniffer(root):
    file_paths = os.listdir(root)
    for file_path in file_paths:
        full_path = os.path.join(root, file_path)
        yield full_path


def filter_data(data):
    data_zero = []
    for name, volatility in data.items():
        if volatility <= 0:
            data_zero.append(name)
    sorted_data = sorted(data.items(), key=lambda element: element[1], reverse=True)
    data_max = (sorted_data[0]), (sorted_data[1]), (sorted_data[2])
    data_min = (sorted_data[len(sorted_data)-1]), (sorted_data[len(sorted_data)-2]), (sorted_data[len(sorted_data)-3])
    data_zero = tuple(data_zero)
    return data_max, data_min, data_zero


def print_result(data_max, data_min, data_zero):
    print(f'Максимальная волатильность:')
    for element in data_max:
        print(f'ТИКЕР {element[0]} - {element[1]}%')
    print(f'Минимальная волатильность:')
    for element in data_min:
        print(f'ТИКЕР {element[0]} - {element[1]}%')
    print(f'Нулевая волатильность:')
    print('{}.'.format(', '.join(data_zero)))
