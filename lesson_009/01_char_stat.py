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
# class CollectingStatistics():
#
#     def __init__(self, file_name):

statistic = {}
count = 0
file_name = 'voyna-i-mir-tom-1.txt'
with open(file_name, 'r', encoding='cp1251') as file:
    for line in file:
        char = ' '
        for char in line:
            # print(char)
            # if char in statistic:
            #     statistic[char] = statistic.get(char) + 1
            # else:
            #     statistic[char] = 1
            if char.isalpha():
                if char.isupper():
                    char = char.lower()
                if char not in statistic:
                    statistic[char] = 1
                else:
                    statistic[char] = statistic.get(char) + 1
        # break

    # print(statistic)
    # print(len(statistic))
# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
