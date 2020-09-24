# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

#  здесь ваш код
sd.resolution = (700, 700)
# print(sd.resolution[1])
for coord_y in range(0, sd.resolution[1]-50, 50):
    # TODO start_point будет у нас всего принимать два значения либо 0 либо -50
    # TODO получать мы его будем используя emunerate + range в первом цикле, получая сразу row, Y в цикле

    # TODO осталось сдвинуть ряд, для этого вам нужно завести переменную start_point и за место первого параметра
    # TODO в range подставить range(start_point, sd.resolution[0]-100, 100)
    for coord_x in range(10, sd.resolution[0]-100, 100):
        left_bottom = sd.get_point(coord_x + 10, coord_y + 7)
        right_top = sd.get_point(100 + coord_x, 50 + coord_y)
        sd.rectangle(left_bottom, right_top, sd.COLOR_WHITE, 5)

# sd.resolution = (1200, 600)
# x, y = 0, 0
# resolution_y = sd.resolution[1] - 50  # вычетаем число кратное стороне y кирпича
# resolution_x = sd.resolution[0] - 100  # вычетаем число кратное стороне x кирпича
# for coord_y in range(0, resolution_y, 50):
#     coord_y += 50
#     for coord_x in range(0, resolution_x, 100):
#         sd.rectangle(left_bottom, right_top, sd.COLOR_WHITE, 5)

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
