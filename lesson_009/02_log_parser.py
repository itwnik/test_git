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

    def parsing(self):
        with open(self.log_name, 'r') as file:  # 'events2.txt'
            for line in file:
                if line[29:32] == 'NOK':
                    event = line[0:17]
                    if event not in self.event_counter:
                        self.event_counter[event] = 1
                    else:
                        self.event_counter[event] = self.event_counter.get(event) + 1

    def writing_file(self):
        with open('parsing_file_out.txt', 'w') as out:
            for error_time, errors_count in self.event_counter.items():
                out.write(f"{error_time}] {errors_count} \n")
        print("Parsing Done!")


test = LogParsing('events2.txt')
test.parsing()
test.writing_file()


# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
