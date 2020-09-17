# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


def sleep_and_cleen(sleep_timer):
    sd.sleep(sleep_timer)
    sd.clear_screen()
    return None


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO не могу понять почему я должен получить точку через функцию get_point
# TODO почему я не могу взять какой нибудт тьюпл? по факту, какого типа переменная center у меня?

for radius in range(50, 65, 5):
    center = sd.get_point(100, 300)
    sd.circle(center, radius)
sleep_and_cleen(2)


# print(type(center))

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет

def print_bub_fun(point_screen, step, color):
    for _ in range(3):
        sd.circle(point_screen, step, color)
        step += 10
    return None


center_1 = sd.get_point(600, 300)
print_bub_fun(center_1, 60, sd.random_color())
sleep_and_cleen(2)

# Нарисовать 10 пузырьков в ряд

for x in range(100, 1100, 100):
    center_2 = sd.get_point(x, 500)
    print_bub_fun(center_2, 50, sd.COLOR_DARK_ORANGE)
sleep_and_cleen(2)

# Нарисовать три ряда по 10 пузырьков

for x in range(200, 1200, 100):
    for y in range(30, 180, 50):
        center_2 = sd.get_point(x, y)
        print_bub_fun(center_2, 5, sd.COLOR_WHITE)
sleep_and_cleen(2)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(99):
    center_3 = sd.random_point()
    radius = sd.random_number(15, 90)
    color = sd.random_color()
    width = sd.random_number(1, 4)
    for _ in range(2):
        sd.circle(center_3, radius, color, width)
        radius += sd.random_number(1, 5)
sleep_and_cleen(5)
sd.quit()

sd.pause()
