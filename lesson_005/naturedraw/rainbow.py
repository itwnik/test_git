# -*- coding: utf-8 -*-

"""
    МОДУЛЬ РИСУЮЩИЙ РАДУГУ
    # Применять разрешение = (1600, 800)
    - тестовый запуск модуля
        sd.resolution = (1600, 800)
        x = 0
        while True:
            x = rainbow_draw(x)
            sd.sleep(0.4)
            if sd.user_want_exit():
                break
        rainbow_draw(0)
        sd.pause()
"""

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
rainbow_colors2 = (sd.COLOR_DARK_RED, sd.COLOR_DARK_ORANGE, sd.COLOR_DARK_YELLOW, sd.COLOR_DARK_GREEN,
                   sd.COLOR_DARK_CYAN, sd.COLOR_DARK_BLUE, sd.COLOR_DARK_PURPLE)


def rainbow_draw(index):
    radius = 1170
    width = 30
    if index > len(rainbow_colors):
        index = 0
    for item, color in enumerate(rainbow_colors2):
        start_point = sd.get_point(600, 0)
        sd.circle(start_point, radius, color, width)
        if index == item:
            sd.circle(start_point, radius, rainbow_colors[index], width)
        radius -= width
        width -= 2
    index += 1
    return index
