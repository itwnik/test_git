# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (800, 600)

for index, coordinate_y in enumerate(range(0, sd.resolution[1], 50)):
    start_point = 0
    if index % 2 == 0:
        start_point = 50
    for coordinate_x in range(start_point, sd.resolution[0], 100):
        left_bottom = sd.get_point(coordinate_x, coordinate_y)
        right_top = sd.get_point(coordinate_x + 100, coordinate_y + 50)
        sd.rectangle(left_bottom,  right_top, color=sd.COLOR_WHITE, width=1)

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()

# зачет!
