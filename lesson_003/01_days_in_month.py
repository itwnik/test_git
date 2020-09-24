# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом

user_input = input('Введите, пожалуйста, номер месяца: ')
if user_input.isdigit():
    month = int(user_input)
    print('Вы ввели', month)
else:
    print('ВЫ ввели не число')
    user_input = input('Введите, пожалуйста, номер месяца: ')

# TODO Сильно большая вложенность, нужно оптимизировать!
#  Использовать списки\словари и проверять на вхождения номера месяца
# TODO и выводить нужный нам ответ

# TODO словарь может выглядеть вот так:

# TODO data_month = {
# TODO     1: число_сколько_дней, (можно добавить список и хранить там нужные данные допустим название еще)
# TODO     ....
# TODO     3: число_сколько_дней,
# TODO     ....
# TODO }


def month_inter(month_num):
    # TODO тут проверяем на вхождение и берем нужные данные и выводим
    if month_num == 1:
        day_count = 31
    elif month_num == 2:
        day_count = 28
    elif month_num == 3:
        day_count = 31
    elif month_num == 4:
        day_count = 30
    elif month_num == 5:
        day_count = 31
    elif month_num == 6:
        day_count = 30
    elif month_num == 7:
        day_count = 31
    elif month_num == 8:
        day_count = 31
    elif month_num == 9:
        day_count = 30
    elif month_num == 10:
        day_count = 31
    elif month_num == 11:
        day_count = 30
    elif month_num == 12:
        day_count = 31
    else:
        print("нет такого месяца")
        day_count = None
    return day_count

# TODO month не определена в этом скоупе
print(month_inter(month))
