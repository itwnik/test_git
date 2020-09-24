# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

#

# тут похоронен здоровый смайл, нарисованный до того как я посмотрел пример)
# def smile(coord_x, coord_y, color):
#     smile_point = simple_draw.get_point(coord_x, coord_y)
#     simple_draw.ellipse(smile_point, 100, color, 2)  # рисуем основу смайла
#     lips_x = simple_draw.get_point(coord_x - 50, coord_y - 50)  # находим точку нач. точкутв круге для отрисовки губ
#     lips_y = simple_draw.get_point(coord_x + 50, coord_y - 50)  # находим точку конеч. точкутв круге для отрисовки губ
#     simple_draw.line(start_point=lips_x, end_point=lips_y)  # рисуем губы
#     eye_left = simple_draw.get_point(coord_x - 30, coord_y + 30)  # находим точку нач. точкутв круге для отрисовки губ
#     eye_right = simple_draw.get_point(coord_x + 30, coord_y + 30)  # находим точку конеч. точкутв круге для отрисовки губ
#     simple_draw.circle(eye_left, 5, color)  # рисуем глаза смайла
#     simple_draw.circle(eye_right, 5, color)  # рисуем глаза смайла

def smile(coord_x, coord_y, color):
    #  основа смайла
    left_bottom = simple_draw.get_point(coord_x, coord_x + 50)  # я тут вообще не понял как я это взял
    right_top = simple_draw.get_point(coord_y, coord_y)
    simple_draw.ellipse(left_bottom, right_top, color, 1)
    eye_left = simple_draw.get_point(coord_x+50, coord_y-30)  # находим точку нач. точкутв круге для отрисовки губ
    eye_right = simple_draw.get_point(coord_x+100, coord_y-30)  # находим точку конеч. точкутв круге для отрисовки губ
    simple_draw.circle(eye_left, 6, color)  # рисуем глаза смайла
    simple_draw.circle(eye_right, 6, color)  # рисуем глаза смайла
    # simple_draw.lines()

smile(30, 200, simple_draw.COLOR_WHITE)

# не могу понять как нарисовать ломанную линию, какие параметры вершин передавать
# так же при отрисовке элипса не понял какие точки у прямоугольникм
# TODO не понял ваших вопросов, если не знаете что передовать можно перейти в функцию и посмотреть что она принимает
# TODO и какие функции еще есть в либе.

# TODO нейминг переменных
x1 = simple_draw.get_point(10, 20)
x2 = simple_draw.get_point(30, 40)
xx = list()
# TODO код падает на этой строке
simple_draw.lines(xx, simple_draw.COLOR_WHITE, closed=False,)

# lips_x = simple_draw.get_point(50, 50)
# print(lips_x)
# lips_y = simple_draw.get_point(coord_y-50, coord_y + 50)
# print(lips_y)
# simple_draw.line(start_point=lips_x, end_point=lips_y)

simple_draw.pause()

# Начиная с третьего модуля буду обращать внимание на то что подчеркивает Пайчар. Придерживаемся PEP8
# Можно привести все к нужному формату code\Reformat code


# TODO Есть недочеты в форматировании по PEP8, используйте пункт меню в пайчарме

# TODO комментарии отладочные удаляем перед пушем!
