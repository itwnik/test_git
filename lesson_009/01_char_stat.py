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

# TODO здесь ваш код
class CollectingStatistics:

    def __init__(self, file_name):
        self.file_name = file_name #'voyna-i-mir-tom-1.txt'
        self.statistic = {}
        self.char = ' '

    def statistics(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for self.char in line:
                    if self.char.isalpha():
                        if self.char.isupper():
                            self.char = self.char.lower()
                        if self.char not in self.statistic:
                            self.statistic[self.char] = 1
                        else:
                            self.statistic[self.char] = self.statistic.get(self.char) + 1

    def output(self):
        # print('+' * 31)
        # print('|{txt:^14}|{txt2:^14}|'.format(txt='Буква', txt2='Частота'))
        # print('+' * 31)
        for count in range(len(self.statistic)):
            print(self.statistic)
        #     print('|{txt:^14}|{txt2:^14}|'.format(txt='Буква', txt2='Частота'))
        # print('+' * 31)
        # print(self.statistic)
        # print(len(self.statistic))


test = CollectingStatistics('voyna-i-mir-tom-1.txt')
test.statistics()
test.output()
    # print(statistic)
    # print(len(statistic))
# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
