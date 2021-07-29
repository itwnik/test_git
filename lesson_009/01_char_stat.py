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

BOOK = 'voyna-i-mir.txt'


class CollectingStatistics:

    def __init__(self, file_name):
        self.file_name = file_name
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

    def sorting_item(self):
        self.statistic = dict(sorted(self.statistic.items(), key=lambda element: element[1]))

    def output(self):
        total_quantity_char = 0
        print('+' * 31)
        print('|{cell_1:^14}|{cell_2:^14}|'.format(cell_1='Буква', cell_2='Частота'))
        print('+' * 31)
        # TODO вот эту часть кода (только цикл) можно вынести сразу в sorting_item
        # TODO тут только вызвать метод self.sorting_item()
        # TODO в самом цикле self.statistic.items() заменить на
        # TODO sorted(self.statistic.items(), key=lambda element: element[1]) который вернут тьюпол
        for char_key, frequency in self.statistic.items():
            print('|{cell_1:^14}|{cell_2:^14}|'.format(cell_1=char_key, cell_2=frequency))
            total_quantity_char = self.statistic[char_key] + total_quantity_char
        print('+' * 31)
        print('|{cell_1:^14}|{cell_2:^14}|'.format(cell_1='Итого', cell_2=total_quantity_char))
        print('+' * 31)

    def starting(self):
        self.file_work()
        self.sorting_item()
        self.output()


# TODO у нас должно получится что с похожей структурой
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

# TODO три дочерних класса в который переопределен только один метод сортировки
# TODO если нужно поправить родительский класс!

class CollectingStatisticsTwo(CollectingStatistics):

    def __init__(self, file_name, flag):
        super().__init__(file_name)
        # self.file_name = file_name
        self.flag = flag

    def sorting_item(self):
        if self.flag == '2':
            self.statistic = dict(sorted(self.statistic.items(), key=lambda element: element[0], reverse=True))  # воз
        else:
            self.statistic = dict(sorted(self.statistic.items(), key=lambda element: element[0], reverse=False))  # убыв


def select_sort_from_user():
    while True:
        user_select_f = input(f"Выберите группировку:\n "
                              f"[1] - по частоте по возрастанию \n"
                              f"[2] - по алфавиту по возрастанию \n"
                              f"[3] - по алфавиту по убыванию \n"
                              )
        if user_select_f.isdigit() and 1 <= int(user_select_f) <= 3:
            return user_select_f
        print(f"Ошибка! повторите ввод!")


if __name__ == '__main__':
    user_select = select_sort_from_user()
    if user_select == '1':  # по частоте по возрастанию
        analysis = CollectingStatistics(BOOK)
    elif user_select == '2':  # по алфавиту по возрастанию
        analysis = CollectingStatisticsTwo(BOOK, user_select)
    else:  # по алфавиту по убыванию
        analysis = CollectingStatisticsTwo(BOOK, user_select)
    analysis.starting()

# метод сортировки долго работает. Как его можно ускорить?
# TODO сильно много преобразований

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
