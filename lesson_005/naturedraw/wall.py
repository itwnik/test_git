# -*- coding: utf-8 -*-

"""

    Модуль рисует стену из кирпичей.
        #  Алгоритм:
        #   цикл по координате Y
        #       проверяем сдвиг ряда кирпичей
        #       цикл координате X
        #           вычисляем правый нижний и левый верхний углы кирпича
        #           рисуем кирпич

start_brick - координаты первого кирпича по х
end_brick - координаты последнего кирпича по х
start_width_brick - начало высоты кирпичной кладки (y)
end_width_brick - конец высоты кирпичной кладки (y)

"""

import simple_draw as sd


def wall_draw(start_brick, end_brick, start_width_brick, end_width_brick, color_brick):
    sd.start_drawing()
    shift = 0
    for index, coordinate_y in enumerate(range(start_width_brick, end_width_brick, 25)):
        if index % 2 == 0:
            shift = 25
        for coordinate_x in range(start_brick+shift, end_brick-shift, 50):
            left_bottom = sd.get_point(coordinate_x, coordinate_y)
            right_top = sd.get_point(coordinate_x + 50, coordinate_y + 25)
            sd.rectangle(left_bottom,  right_top, color=color_brick, width=1)
            shift = 0
    sd.finish_drawing()


# wall_draw(start_brick=300, end_brick=900, start_width_brick=50, end_width_brick=400)
