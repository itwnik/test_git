# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class LogParsing:

    def __init__(self, log_name):
        self.log_name = log_name
        self.event_counter = {}
        self.pars_param = 'NOK'
        self.count = 0

    def parsing(self, line):
        if line[29:32] == self.pars_param:
            self.count += 1
            event = line[0:17]
            if event not in self.event_counter:
                self.event_counter[event] = 1
            else:
                self.event_counter[event] = self.event_counter.get(event) + 1

    # TODO как и ранее все логика по дефолту должна быть в этом классе
    # TODO вам нужно написать или вынести часть кода в отдельный метод сортировки

class FileWorks(LogParsing):

    def reading_file(self):
        with open(self.log_name, 'r') as file:  # 'events.txt'
            for line in file:
                self.parsing(line)

    def writing_file(self):
        # TODO почему используйте кодировку cp1251 ? используем utf8
        with open('parsing_file_out.txt', 'w', encoding='cp1251') as out:
            for error_time, errors_count in self.event_counter.items():
                out.write(f"{error_time}] {errors_count} \n")
            out.write(f" Общее количество ошиибок {self.count}")
        print("Parsing Done!")


parsing_file = FileWorks('events.txt')
parsing_file.reading_file()
parsing_file.writing_file()


# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
