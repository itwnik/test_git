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

LOG_NAME = 'events.txt'
PARSING_PARAMETER = 'NOK'


class LogParsing:

    def __init__(self, log_name, parsing_param):
        self.log_name = log_name
        self.event_counter = {}
        self.pars_param = parsing_param
        self.pars_string = ''
        self.count = 0

    def reading_file(self):
        with open(self.log_name, 'r') as file:
            for line in file:
                if line[29:32] == self.pars_param:
                    self.pars_string_information(line)
                    self.parsing(self.pars_string)

    def pars_string_information(self, line):
        self.pars_string = line[0:17]

    def parsing(self, cropped_line):
        self.count += 1
        if cropped_line not in self.event_counter:
            self.event_counter[cropped_line] = 1
        else:
            self.event_counter[cropped_line] = self.event_counter.get(cropped_line) + 1

    def writing_file(self):
        with open('parsing_file_out.txt', 'w', encoding='utf8') as out:
            for error_time, errors_count in self.event_counter.items():
                out.write(f"{error_time}] {errors_count} \n")
            out.write(f" Общее количество ошиибок {self.count}")
        print("Parsing Done!")

    def starting(self):
        self.reading_file()
        self.writing_file()


class LogParsingTwo(LogParsing):

    def pars_string_information(self, line):
        self.pars_string = line[0:14]  # по часу


class LogParsingThree(LogParsing):

    def pars_string_information(self, line):
        self.pars_string = line[0:8]  # по месяц


class LogParsingFour(LogParsing):

    def pars_string_information(self, line):
        self.pars_string = line[0:5]  # по году


def select_sort_from_user():
    while True:
        user_select_f = input(f"Выберите группировку: \n "
                              f"[1] - по часам \n [2] - по месяцу \n [3] - по году \n [4] - по минутам \n")
        if user_select_f.isdigit() and 1 <= int(user_select_f) <= 4:
            return user_select_f
        print(f"Ошибка! повторите ввод!")


if __name__ == '__main__':
    user_select = select_sort_from_user()
    if user_select == '1':  # по часам
        parsing_file = LogParsingTwo(LOG_NAME, PARSING_PARAMETER)
    elif user_select == '2':  # по месяцу
        parsing_file = LogParsingThree(LOG_NAME, PARSING_PARAMETER)
    elif user_select == '3':  # по году
        parsing_file = LogParsingFour(LOG_NAME, PARSING_PARAMETER)
    else:
        parsing_file = LogParsing(LOG_NAME, PARSING_PARAMETER)
    parsing_file.starting()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
