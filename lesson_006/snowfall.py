# -*- coding: utf-8 -*-

import simple_draw as sd

settings_snowflake = []
fall_snow = []


def create_snowflake(count):
    global settings_snowflake
    for _ in range(count):
        x = sd.random_number(100, 1100)
        y = sd.random_number(500, 550)
        length = sd.random_number(20, 30)
        settings_snowflake.append([x, y, length])
    return count

# TODO во всех остальных функциях можнно не указывать global settings_snowflake!?
#   по идеи все остальные функции берут информацию из глобального списка так как своего такого у них нет!?


def paint_color_snowflake(snowflake_color):
    global settings_snowflake
    sd.start_drawing()
    for index in range(len(settings_snowflake)):
        point_x, point_y = settings_snowflake[index][0], settings_snowflake[index][1]  # распаковываем х,y в переменную
        length_snow = settings_snowflake[index][2]  # распаковываем длину в переменную
        center_snowflake = sd.get_point(point_x, point_y)  # получаем центр снежинки
        sd.snowflake(center_snowflake, length=length_snow, color=snowflake_color)  # рисуем синим снежинку
    sd.finish_drawing()


def shift_snowflake():
    global settings_snowflake
    for index in range(len(settings_snowflake)):
        settings_snowflake[index][0] += sd.random_number(-15, 15)  # меняем х
        settings_snowflake[index][1] -= sd.random_number(15, 25)  # меняем у
        # settings_snowflake[index][2] -= sd.random_number(-5, 5)  # меняем length


def index_fall_snow():
    temp = False
    for index in range(len(settings_snowflake)):
        if settings_snowflake[index][1] <= -50:
            fall_snow.append(index)
            temp = True
    return temp


def del_snowflake():
    global fall_snow
    for index, elem in enumerate(fall_snow):
        settings_snowflake.pop(elem-index)
    length_fall_snow = len(fall_snow)
    fall_snow.clear()
    return length_fall_snow
