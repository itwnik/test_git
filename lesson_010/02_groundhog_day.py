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


count = 0
karma_quantity = 0

# TODO создайте константу список в котором будут храниться имена class ов чтобы их потом можно было выбрать и вызвать!
# TODO имена классов храним без их вызовов () и сообщений, сами сообщения будем формировать в главном цикле
error = [IamGodError('Эта Ошибка Божествнна!'),
         DrunkError('Ошибка: Балтика 9! И пусть весь мир подождет'),
         CarCrashError('Ошибка: была когда ты сел за руль этой Калины!'),
         GluttonyError('Ошибка: Переел в Макдональдсе'),
         DepressionError('Ошибка: Depression detect!'),
         SuicideError('Они убили Кенни')]


# TODO функция one_day() должна возвращать карму от 1 до 7 или рейзит ошибку из расчета 1 к 13
# TODO мы можем объявить 2 переменные это карма равная рендинт от 1 до 7 и
# TODO сам еррор который тоже равен рендинт от 1 до 13
# TODO далее условие если еррор равен 13 то мы choice выбираем случайное исключение из списка
# TODO и его рейзим как объект используя ()
# TODO если условие не сработало то мы ретурним карму
def one_day():
    # TODO без глобал
    global karma_quantity
    karma_quantity += rd.randint(1, 7)
    probability = rd.randint(1, 13)
    if probability == 13:
        raise rd.choice(error)


 while karma_quantity <= ENLIGHTENMENT_CARMA_LEVEL:
    try:
        one_day()
    # TODO написать отдельную функцию записи, тут будем наполнять список, формируя нужную стоку
    # TODO в конце цикла нужно запустить функцию записи
    # TODO строку формируем на каждой ошибке свою
    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
        count += 1
        print(f"{count}. Error Detected {type(exc)}: {exc}, Карма = {karma_quantity}")
    # TODO можно достучаться до имени класса через меджик метод __init__
    # как убрать "<class '__main__." в выводе типа своей ошибки?
print(f"Количество зарегистрированных ошибок: {count}")
print(f"Карма достикла уровня ПРОСВЕТЛЕНИЯ и = {karma_quantity}, день сурка закончен!")

# https://goo.gl/JnsDqu
