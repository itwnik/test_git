# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall as sf

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall
sd.resolution = (1200, 600)
N = 20
# создать_снежинки(N)
sf.create_snowflake(N)
while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    sf.paint_color_snowflake(snowflake_color=sd.background_color)
    #  сдвинуть_снежинки()
    sf.shift_snowflake()
    #  нарисовать_снежинки_цветом(color)
    sf.paint_color_snowflake(snowflake_color=sd.COLOR_WHITE)
    #  если есть номера_достигших_низа_экрана() то
    if sf.index_fall_snow():
        # удалить_снежинки(номера)
        # TODO тут что то нужно сделать с неймингом N
        N = sf.del_snowflake()
        # создать_снежинки(count)
        # TODO добавлять будем столько сколько sf.index_fall_snow() вернет используя len()
        sf.create_snowflake(N)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
