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
    # TODO для чего мы вернули count ?
    return count

# TODO global указывает функции что мы используем глобальную переменную и изменять будем ее, если мы просто используем
# TODO переменную и она у нас объявлена в глобальном скоупе как строкой 5 то global можно и опустить так нет в ней
# TODO необходимости! мы и так прочитаем переменную не изменяя ее! Поправить везде!


def paint_color_snowflake(snowflake_color):
    global settings_snowflake
    # TODO старт и финищ используем в главном цикле!
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
    # TODO это лишняя переменная
    temp = False
    for index in range(len(settings_snowflake)):
        if settings_snowflake[index][1] <= -50:
            fall_snow.append(index)
            temp = True
    # TODO тут мы должны возвращать список индексов! Что бы в главном модуле определить его длинну!
    return temp


def del_snowflake():
    global fall_snow
    for index, elem in enumerate(fall_snow):
        # TODO используем либо del \ remove поскольку pop возвращает! но мы ничего не принимаем!
        settings_snowflake.pop(elem-index)
    length_fall_snow = len(fall_snow)
    # TODO очищать список нужно будем в create_snowflake
    fall_snow.clear()
    # TODO тут мы возвращать ничего не должны!
    return length_fall_snow
