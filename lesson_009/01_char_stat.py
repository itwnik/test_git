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
        self.total_quantity_char = 0

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
        for char_key, frequency in sorted(self.statistic.items(), key=lambda element: element[1]):
            print('|{cell_1:^14}|{cell_2:^14}|'.format(cell_1=char_key, cell_2=frequency))
            self.total_quantity_char = self.statistic[char_key] + self.total_quantity_char

    def output(self):
        print('+' * 31)
        print('|{cell_1:^14}|{cell_2:^14}|'.format(cell_1='Буква', cell_2='Частота'))
        print('+' * 31)
        self.sorting_item()
        print('+' * 31)
        print('|{cell_1:^14}|{cell_2:^14}|'.format(cell_1='Итого', cell_2=self.total_quantity_char))
        print('+' * 31)

    def starting(self):
        self.file_work()
        self.output()


# TODO  Упорядочивание по частоте - по убыванию это в родительском классе
# TODO далее три дочерних
# TODO
#   - по частоте по возрастанию
#   - по алфавиту по возрастанию
#   - по алфавиту по убыванию

#  Почему три дочерних класса? сортировка по частоте у нас в родительском классе.
#  и 2 дочерних "по алфавиту возрастанию" и "по по алфавиту по убыванию". Так ведь?


class CollectingStatisticsTwo(CollectingStatistics):

    def sorting_item(self):
        for char_key, frequency in sorted(self.statistic.items(), key=lambda element: element[0], reverse=True):  # воз
            print('|{cell_1:^14}|{cell_2:^14}|'.format(cell_1=char_key, cell_2=frequency))
            self.total_quantity_char = self.statistic[char_key] + self.total_quantity_char


class CollectingStatisticsThree(CollectingStatistics):

    def sorting_item(self):
        for char_key, frequency in sorted(self.statistic.items(), key=lambda element: element[0], reverse=False):  # уб
            print('|{cell_1:^14}|{cell_2:^14}|'.format(cell_1=char_key, cell_2=frequency))
            self.total_quantity_char = self.statistic[char_key] + self.total_quantity_char


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
        analysis = CollectingStatisticsTwo(BOOK)
    else:  # по алфавиту по убыванию
        analysis = CollectingStatisticsThree(BOOK)
    analysis.starting()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
