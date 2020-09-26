# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def emoji(coord_x, coord_y, color):
    #  основа смайла
    _smile_center = simple_draw.get_point(coord_x, coord_y)
    simple_draw.circle(_smile_center, 30)
    #  глаза смайла
    _eye_left = simple_draw.get_point(coord_x - 10, coord_y + 10)  # находим центр левого глаза
    _eye_right = simple_draw.get_point(coord_x + 10, coord_y + 10)  # находим центр правого глаза
    simple_draw.circle(_eye_left, 5, color)  # рисуем левый глаза смайла
    simple_draw.circle(_eye_right, 5, color)  # рисуем правый глаза смайла
    #  губы смайла
    _lips_point1 = simple_draw.get_point(coord_x - 10, coord_y - 10)  # находим точку нач. точкутв круге для губ
    _lips_point2 = simple_draw.get_point(coord_x - 7, coord_y - 15)  # находим точку точкут для губ
    _lips_point4 = simple_draw.get_point(coord_x + 10, coord_y - 10)  # находим точку конеч. точкутв круге для губ
    simple_draw.lines([_lips_point1, _lips_point2, _lips_point4])  # 3 точки - это не ошибка а так задумано_)


# TODO прошу подсказать, как получить точку х или y из функции .get_point
# TODO пробовал так
# TODO point = simple_draw.get_point(100, 50)
# TODO point(0) или так point[0] не выходит
for _ in range(10):
    coordinate_x = simple_draw.random_number(100, 600)
    coordinate_y = simple_draw.random_number(150, 650)
    emoji(coord_x=coordinate_x, coord_y=coordinate_y, color=simple_draw.COLOR_WHITE)

simple_draw.pause()
