# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class CollectingStatistics:

    def __init__(self, file_name):
        self.file_name = file_name  # 'voyna-i-mir-tom-1.txt'
        self.statistic = {}
        self.char = ' '

    def file_work(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for self.char in line:
                    self.statistics()

    def statistics(self):
        if self.char.isalpha():
            if self.char not in self.statistic:
                self.statistic[self.char] = 1
            else:
                self.statistic[self.char] = self.statistic.get(self.char) + 1


    def sorting_item(self):  # TODO Определения методов отделяются от остального кода одной пустой строкой
        output_data = list(self.statistic.items())
        output_data.sort(key=lambda element: element[1])
        self.statistic = dict(output_data)

    def output(self):
        self.sorting_item()
        total_quantity_char = 0
        print('+' * 31)
        print('|{cell_1:^14}|{cell_2:^14}|'.format(cell_1='Буква', cell_2='Частота'))
        print('+' * 31)
        for char_key, frequency in self.statistic.items():
            print('|{cell_1:^14}|{cell_2:^14}|'.format(cell_1=char_key, cell_2=frequency))
            total_quantity_char = self.statistic[char_key] + total_quantity_char
        print('+' * 31)
        print('|{cell_1:^14}|{cell_2:^14}|'.format(cell_1='Итого', cell_2=total_quantity_char))
        print('+' * 31)
    # TODO Для реализации паттерна необходимо разбить всю выполняемую задачу на отдельные шаги:
    #  1) получение данных (тут может быть подготовка файла - его разахивация, при необходимости),
    #  2) сбор даннных - подсчёт частоты использования букв,
    #  3) сортировка статистических данных,
    #  4) вывод в консоль таблицы с данными.
    #  Также потребуется сам "шаблонный метод", где последовательно вызываются все методы по порядку.
    #    а) подготовка файла (разархивация, при необходимости)
    #    б) сбор данных из файла
    #    в) сортировка
    #    г) вывод в консоль
    #  Имя шаблонного метода должно быть кратким, например: "запустить", "выполнить"


#  теперь да))  до этого свой файл качал, не заметил его в сниппетах
analysis = CollectingStatistics('voyna-i-mir.txt')
# TODO Имена файлов надо присваивать константам и использовать в основном коде только их.
#  Имена констант пишутся большими буквами. Располагают константы в начале модуля, сразу после
#  импортов сторонних модулей.
#  Может возникнуть необходимость изменить имя файла и через константу это делать удобнее - константа это
#  единое место изменения, а примениться она может во многих местах. Поэтому вверху её легко найти для изменения
#  без необходимости перелопачивания кода проекта.

analysis.file_work()
analysis.output()
# TODO тут должен быть вызван только один метод - шаблонный

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
