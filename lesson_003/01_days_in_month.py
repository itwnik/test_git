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


def month_inter(month_num):
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


print(month_inter(month))
