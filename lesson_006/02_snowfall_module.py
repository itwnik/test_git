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
amount_snow = 20
# создать_снежинки(N)
sf.create_snowflake(amount_snow)
while True:
    sd.start_drawing()
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    sf.paint_color_snowflake(snowflake_color=sd.background_color)
    #  сдвинуть_снежинки()
    sf.shift_snowflake()
    #  нарисовать_снежинки_цветом(color)
    sf.paint_color_snowflake(snowflake_color=sd.COLOR_WHITE)
    #  если есть номера_достигших_низа_экрана() то
    sd.finish_drawing()
    if sf.index_fall_snow():
        # удалить_снежинки(номера)
        amount_snow = sf.del_snowflake()
        # создать_снежинки(count)
        # TODO в первоночальном варианте я хотел так сделать, но меня смутило то, что "зачем вызывать повторно функцию
        #   если я уже ее вызываю в if"
        sf.create_snowflake(len(sf.index_fall_snow()))
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
