# -*- coding: utf-8 -*-

import simple_draw

"""
    Модуль отрисовки смайлика по заданным координатам
    Параметры функции: кордината X, координата Y, цвет.
    - тестовый запуск модуля
    while True:
        emoji(coord_x=300, coord_y=300, color=simple_draw.COLOR_YELLOW)
        simple_draw.sleep(0.4)
        if simple_draw.user_want_exit():
            break
    simple_draw.pause()
"""


def emoji(coord_x, coord_y, color):
    event = simple_draw.random_number(0, 1)
    #  основа смайла
    _smile_center = simple_draw.get_point(coord_x, coord_y)
    simple_draw.circle(_smile_center, radius=50, color=simple_draw.background_color, width=0)
    simple_draw.circle(_smile_center, radius=50)
    #  глаза смайла
    _eye_left = simple_draw.get_point(coord_x - 17, coord_y + 15)  # находим центр левого глаза
    _eye_right = simple_draw.get_point(coord_x + 17, coord_y + 15)  # находим центр правого глаза
    if event == 0:
        close = False
        simple_draw.circle(_eye_left, 7, color)  # рисуем левый глаза смайла
        simple_draw.circle(_eye_right, 7, color)  # рисуем правый глаза смайла
    else:
        close = True
        simple_draw.circle(_eye_left, 7, color)   # рисуем левый глаза смайла
        _eye_right_1 = simple_draw.get_point(coord_x + 10, coord_y + 15)  # находим начало правого глаза
        _eye_right_2 = simple_draw.get_point(coord_x + 20, coord_y + 15)  # находим конец правого глаза
        simple_draw.line(_eye_right_1, _eye_right_2, width=2)  # рисуем правый глаза смайла
    #  губы смайла
    _lips_point1 = simple_draw.get_point(coord_x - 15, coord_y - 15)  # находим точку нач. точкутв круге для губ
    _lips_point2 = simple_draw.get_point(coord_x - 7, coord_y - 25)  # находим точку точкут для губ
    _lips_point4 = simple_draw.get_point(coord_x + 20, coord_y - 15)  # находим точку конеч. точкутв круге для губ
    simple_draw.lines([_lips_point1, _lips_point2, _lips_point4], closed=close)  # 3 точки-это не ошибка а так задумано)

