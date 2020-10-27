# -*- coding: utf-8 -*-

"""
    МОДУЛЬ РИСУЮЩИЙ РАДУГУ
    # Применять разрешение = (1600, 800)
"""

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def rainbow_draw():
    radius = 1170
    width = 30
    for color in rainbow_colors:
        start_point = sd.get_point(600, 0)
        sd.circle(start_point, radius, color, width)
        radius -= width
        width -= 2


# rainbow_draw()
