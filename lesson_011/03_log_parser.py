# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

LOG_NAME = 'events.txt'
PARSING_PARAMETER = 'NOK'

# ## Generator ##
# def event_generator(log_name):
#     count_generator = 0
#     current_date = ''
#     previous_date = ''
#     with open(log_name, 'r', encoding='utf-8') as file_event:
#         for file_line in file_event:
#             if file_line[29:32] == PARSING_PARAMETER:
#                 current_date = file_line[0:17]
#                 if previous_date == '':
#                     previous_date = current_date
#                 if current_date == previous_date:
#                     count_generator += 1
#                 else:
#                     yield previous_date, count_generator
#                     count_generator = 1
#                     previous_date = current_date
#         yield current_date, count_generator


# ## Iterator ##
class EventGenerator:

    def __init__(self, log_name):
        self.log_name = log_name

    def __iter__(self):
        self.count_generator = 0
        self.current_date = ''
        self.previous_date = ''
        self.file_event = open(self.log_name, 'r', encoding='utf-8')
        return self

    def __next__(self):
        if self.file_event.closed:
            raise StopIteration
        for file_line in self.file_event:
            if file_line[29:32] == PARSING_PARAMETER:
                self.current_date = file_line[0:17]
                if self.previous_date == '':
                    self.previous_date = self.current_date
                if self.current_date == self.previous_date:
                    self.count_generator += 1
                    self.previous_date = self.current_date
                else:
                    memory1 = self.count_generator
                    memory2 = self.previous_date
                    self.count_generator = 1
                    self.previous_date = self.current_date
                    return memory2, memory1
        self.file_event.close()
        return self.previous_date, self.count_generator


# ## Iterator ##
grouped_events = EventGenerator(LOG_NAME)
# ## Generator ##
# grouped_events = event_generator(LOG_NAME)
for group_time, event_count in grouped_events:
    print(f'{group_time}] {event_count}')

# TODO Посмотрели и генератор и итератор?
