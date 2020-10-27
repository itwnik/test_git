# -*- coding: utf-8 -*-

import simple_draw as sd

N = 7

settings_snowflake = []
for _ in range(N):
    x = sd.random_number(20, 200)
    y = sd.random_number(500, 600)
    length = sd.random_number(15, 25)
    settings_snowflake.append([x, y, length])


def snow():
    end = 50
    while True:
        sd.start_drawing()
        for index in range(N):
            point_x = settings_snowflake[index][0]  # распаковываем х в переменную
            point_y = settings_snowflake[index][1]  # распаковываем у в переменную
            length_snow = settings_snowflake[index][2]  # распаковываем длину в переменную
            center_snowflake = sd.get_point(point_x, point_y)  # получаем центр снежинки
            sd.snowflake(center_snowflake, length=length_snow, color=sd.background_color)  # рисуем синим снежинку синим
            point_x += sd.random_number(-15, 15)  # меняем х
            point_y -= sd.random_number(15, 25)  # меняем у
            center_snowflake = sd.get_point(point_x, point_y)  # получаем центр новой снежинки
            sd.snowflake(center=center_snowflake, length=length_snow)  # рисуем новую снежинку белым цветом
            # можно одной строкой!
            settings_snowflake[index] = [point_x, point_y, length_snow]
            if point_y < end:  # если у меньш почти конца экрана
                settings_snowflake[index][1] = 600  # в списке у определяем в начала экрана
                end += 1  # увеличиваем почти конец экрана
            sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():  # проверка выхода из цикла
            break

# sd.pause()

# Это сделано специально для удобочитаемости кода, чтобы было понятно и вам и тому кто будем его читать!
# + Логика такая что мы сначала взяли нужные данные и работаем с ними, как только они нам не нужны мы их обновили!
# можно сделать вот так 136 строка.
# В дальнейшем нам этот код еще пригодиться!

# зачет!
