# -*- coding: utf-8 -*-

import simple_draw as sd

settings_snowflake = []
fall_snow = []


def create_snowflake(count):
    global settings_snowflake
    fall_snow.clear()
    for _ in range(count):
        x = sd.random_number(100, 1100)
        y = sd.random_number(500, 550)
        length = sd.random_number(20, 30)
        settings_snowflake.append([x, y, length])


def paint_color_snowflake(snowflake_color):
    for index in range(len(settings_snowflake)):
        point_x, point_y = settings_snowflake[index][0], settings_snowflake[index][1]  # распаковываем х,y в переменную
        length_snow = settings_snowflake[index][2]  # распаковываем длину в переменную
        center_snowflake = sd.get_point(point_x, point_y)  # получаем центр снежинки
        sd.snowflake(center_snowflake, length=length_snow, color=snowflake_color)  # рисуем синим снежинку


def shift_snowflake():
    global settings_snowflake
    for index in range(len(settings_snowflake)):
        settings_snowflake[index][0] += sd.random_number(-15, 15)  # меняем х
        settings_snowflake[index][1] -= sd.random_number(15, 25)  # меняем у
        # settings_snowflake[index][2] -= sd.random_number(-5, 5)  # меняем length


def index_fall_snow():
    global fall_snow
    for index in range(len(settings_snowflake)):
        if settings_snowflake[index][1] <= -50:
            fall_snow.append(index)
    return fall_snow


# если снежинки будут залипать нужно fall_snow отсортировать и перевернуть
# TODO что значит если снежинка будет залипать? не понял немного.
def del_snowflake():
    global settings_snowflake
    for elem in fall_snow:
        del settings_snowflake[elem-fall_snow.index(elem)]
