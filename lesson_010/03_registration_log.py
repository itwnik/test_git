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
    elif int(pars_text[2]) < 10 or int(pars_text[2]) > 99:
        message = " ".join(pars_text)
        raise ValueError('поле возраст НЕ является числом от 10 до 99')
    else:
        message = " ".join(pars_text)


def output_files(out_log_name, outs_log):
    with open(out_log_name, 'w', encoding='utf8') as out_log_file:
        for item in outs_log:
            out_log_file.write(f"{item}")


message = ''
goods_log = []
bads_log = []

with open(FILE, 'r', encoding='utf-8') as file:
    for line in file:
        try:
            file_check(line)
            goods_log.append(message)
        except (ValueError, NotNameError, NotEmailError) as exc:
            out_test = " {} {} {}\n".format(message.rstrip('\n'), str(type(exc)),  str(exc.args[0]))
            bads_log.append(out_test)
output_files('registrations_good.log', goods_log)
output_files('registrations_bad.log', bads_log)
print("Parsing done!")

# зачет!
