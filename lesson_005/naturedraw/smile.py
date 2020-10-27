# -*- coding: utf-8 -*-

import simple_draw

"""
    Модуль отрисовки смайлика по заданным координатам
    Параметры функции: кордината X, координата Y, цвет.
"""


def emoji(coord_x, coord_y, color):
    #  основа смайла
    _smile_center = simple_draw.get_point(coord_x, coord_y)
    simple_draw.circle(_smile_center, 50)
    #  глаза смайла
    _eye_left = simple_draw.get_point(coord_x - 17, coord_y + 15)  # находим центр левого глаза
    _eye_right = simple_draw.get_point(coord_x + 17, coord_y + 15)  # находим центр правого глаза
    simple_draw.circle(_eye_left, 7, color)  # рисуем левый глаза смайла
    simple_draw.circle(_eye_right, 7, color)  # рисуем правый глаза смайла
    #  губы смайла
    _lips_point1 = simple_draw.get_point(coord_x - 15, coord_y - 15)  # находим точку нач. точкутв круге для губ
    _lips_point2 = simple_draw.get_point(coord_x - 7, coord_y - 25)  # находим точку точкут для губ
    _lips_point4 = simple_draw.get_point(coord_x + 20, coord_y - 15)  # находим точку конеч. точкутв круге для губ
    simple_draw.lines([_lips_point1, _lips_point2, _lips_point4])  # 3 точки - это не ошибка а так задумано_)
