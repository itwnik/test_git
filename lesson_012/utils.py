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


def filter(data):
    data_max = {}
    data_min = {}
    # TODO у вас есть тьюпол после sorted к дикту не приводим
    # TODO сразу срезами берем первые 3 элемента и крайние 3 элемента
    sorted_data = dict(sorted(data.items(), key=lambda element: element[1], reverse=True))
    # return sorted_data
    for item in range(0, 3):
        data_max[list(sorted_data.keys())[item]] = list(sorted_data.values())[item]
    for item in range(len(sorted_data)-1, len(sorted_data)-4, -1):
        data_min[list(sorted_data.keys())[item]] = list(sorted_data.values())[item]
    return data_max, data_min

    #  ну тут я из большого словаря валентностей делаю 2 маленьких словоря,
    #  впервый я переношу первые 3 максимальные валентности, во второй последние 3 минимальные.
    #  не спрашивайте зачем) мне поазалось просто так удобнее.
    #  вопрос есть ли какой нибудь простой способ из одного словаря перетащить n элементов в другой?
    #  или как упростить мой код?
    # у вас тут происходит ?
    # есть ли способы уменьшить код?


def print_result(data_max, data_min, data_zero):
    print(f'Максимальная волатильность:')
    # TODO тут передаем на вход не словарь а тьюпол и items() убрать
    for key, value in data_max.items():
        print(f'ТИКЕР {key} - {value}%')
    print(f'Минимальная волатильность:')
    for key, value in data_min.items():
        print(f'ТИКЕР {key} - {value}%')
    print(f'Нулевая волатильность:')
    print('{}.'.format(', '.join(data_zero.keys())))
