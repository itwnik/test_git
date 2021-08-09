# -*- coding: utf-8 -*-

"""
# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
"""

FILE = 'registrations.txt'


class NotNameError(ValueError):
    pass


class NotEmailError(ValueError):
    pass


def file_check(check_line):
    global message
    pars_text = check_line.split(' ')
    if len(pars_text) != 3:
        message = " ".join(pars_text)
        raise ValueError('НЕ присутсвуют все три поля')
    elif not pars_text[0].isalpha():
        message = " ".join(pars_text)
        raise NotNameError('поле имени содержит НЕ только буквы')
    elif pars_text[1].count('@') != 1 and pars_text[1].count('.') != 1:
        message = " ".join(pars_text)
        raise NotEmailError('поле емейл НЕ содержит @ и .(точку)')
    elif int(pars_text[2]) <= 10 or int(pars_text[2]) >= 99:
        message = " ".join(pars_text)
        raise ValueError('поле возраст НЕ является числом от 10 до 99')
    else:
        message = " ".join(pars_text)


# TODO функция должна принимать на вход одно имя и один список
def output_files(out_good, out_bad):
    # TODO записывать только один файл
    with open('registrations_good.log', 'w', encoding='utf8') as out_good_log,\
         open('registrations_bad.log', 'w', encoding='utf8') as out_bad_log:
        for item in out_good:
            out_good_log.write(f"{item}")
        for item in out_bad:
            out_bad_log.write(f"{item}")


message = ''
# TODO принято добавлять S в конец имени чтобы было понятно что это список, и назвать более развернуто
good = []
bad = []

with open(FILE, 'r', encoding='utf-8') as file:
    for line in file:
        try:
            file_check(line)
            good.append(message)
        except (ValueError, NotNameError, NotEmailError) as exc:
            out_test = " {} {} {}\n".format(message.rstrip('\n'), str(type(exc)),  str(exc.args[0]))
            bad.append(out_test)

# TODO но в коде вот тут нужно вызывать ее 2 раза с разными именами и данными на запись
output_files(good, bad)
print("Parsing done!")
