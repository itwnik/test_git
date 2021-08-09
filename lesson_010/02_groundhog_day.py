# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

import random as rd
import os

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(BaseException):
    pass


class DrunkError(ValueError):
    pass


class CarCrashError(SystemError):
    pass


class GluttonyError(TypeError):
    pass


class DepressionError(ReferenceError):
    pass


class SuicideError(FileExistsError):
    pass


ERROR = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]
karma = 0
count = 0
error_logs = []


def one_day():
    karma_quantity = rd.randint(1, 7)
    error = rd.randint(1, 13)
    if error == 13:
        raise rd.choice(ERROR)()
    else:
        return karma_quantity


def error_log(error_code):
    message = ''
    if error_code.__class__.__name__ == 'IamGodError':
        message = 'Эта Ошибка Божествнна!'
    elif error_code.__class__.__name__ == 'DrunkError':
        message = 'Ошибка: Балтика 9! И пусть весь мир подождет'
    elif error_code.__class__.__name__ == 'CarCrashError':
        message = 'Ошибка: была когда ты сел за руль этой Калины!'
    elif error_code.__class__.__name__ == 'GluttonyError':
        message = 'Ошибка: Переел в Макдональдсе'
    elif error_code.__class__.__name__ == 'DepressionError':
        message = 'Ошибка: Depression detect!'
    elif error_code.__class__.__name__ == 'SuicideError':
        message = 'Они убили Кенни!'
    error_logs.append(f"{count}. Error Detected {exc.__class__.__name__}: {message}, Карма = {karma}")
    # TODO код на запись выносим в отдельную функцию вызываем после главного цикла передаем список на запись
    # TODO добавить аргумент encoding='utf8'
    with open('error.log', 'w') as file:
        for item in error_logs:
            file.write(f"{item}\n")


while karma <= ENLIGHTENMENT_CARMA_LEVEL:
    try:
        karma += one_day()
    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
        count += 1
        error_log(exc)

# все верно

print(f"Количество зарегистрированных ошибок: {count}")
print(f"Карма достикла уровня ПРОСВЕТЛЕНИЯ и = {karma}, день сурка закончен!")
print("log create!")
os.startfile('error.log')

# https://goo.gl/JnsDqu
