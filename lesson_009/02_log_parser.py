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

    def reading_file(self):
        with open(self.log_name, 'r') as file:  # 'events.txt'
            for line in file:
                self.parsing(line)

    def writing_file(self):
        self.sorting(self.select_sort_from_user())
        with open('parsing_file_out.txt', 'w', encoding='utf8') as out:
            for error_time, errors_count in self.event_counter.items():
                out.write(f"{error_time}] {errors_count} \n")
            out.write(f" Общее количество ошиибок {self.count}")
        print("Parsing Done!")

    def select_sort_from_user(self):
        while True:
            user_select = input(f"Выбирите группировку: \n [1] - по часам \n [2] - по месяцу \n [3] - по году \n")
            if user_select.isdigit() and 1 <= int(user_select) <= 3:
                return user_select
            print(f"Ошибка! повторите ввод!")

    def sorting(self, user_select):
        if user_select == '1':  # по часу
            start_sorting_position, end_sorting_position = 12, 14
        elif user_select == '2':  # по месяцу
            start_sorting_position, end_sorting_position = 6, 8
        elif user_select == '3':  # по году
            start_sorting_position, end_sorting_position = 1, 5
        output_data_sorting = list(self.event_counter.items())
        output_data_sorting.sort(key=lambda element: element[0][start_sorting_position:end_sorting_position])
        self.event_counter = dict(output_data_sorting)

    # TODO т.е. у нас будет 1 класс? и внем отдельно меттод сортировки? так?
    # TODO тогда в чем фишка шаблонного метода?


parsing_file = LogParsing('events.txt')
parsing_file.reading_file()
parsing_file.writing_file()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
