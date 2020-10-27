# -*- coding: utf-8 -*-

"""
    Модуль рисует дом с кирпичной стеной и окном.
    в модуле используются функции модуля wall.py из пакета naturedraw.
"""

import naturedraw.wall as wl
import simple_draw as sd

sd.resolution = (1200, 800)

colors = {0: ['WHITE', sd.COLOR_WHITE],
          1: ['BLACK', sd.COLOR_BLACK],
          2: ['RED', sd.COLOR_RED],
          3: ['ORANGE', sd.COLOR_ORANGE],
          4: ['YELLOW', sd.COLOR_YELLOW],
          5: ['GREEN', sd.COLOR_GREEN],
          6: ['CYAN', sd.COLOR_CYAN],
          7: ['BLUE', sd.COLOR_BLUE],
          8: ['PURPLE', sd.COLOR_PURPLE],
          9: ['DARK YELLOW', sd.COLOR_DARK_YELLOW],
          10: ['DARK ORANGE', sd.COLOR_DARK_ORANGE],
          11: ['DARK RED', sd.COLOR_DARK_RED],
          12: ['DARK GREEN', sd.COLOR_DARK_GREEN],
          13: ['DARK CYAN', sd.COLOR_DARK_CYAN],
          14: ['DARK BLUE', sd.COLOR_DARK_BLUE],
          15: ['DARK PURPLE', sd.COLOR_DARK_PURPLE],
          16: ['НивиДимки =)', sd.background_color]}


def paint_rectangle(x1, y1, x2, y2, color, width):  # функция каркаса дома и окна
    start_home_point = sd.get_point(x1, y1)
    end_home_point = sd.get_point(x2, y2)
    sd.rectangle(start_home_point, end_home_point, color=colors[color][1], width=width)


def home_window_roof():  # функция отрисовки дома с окном и крышей
    # рисуем карас дома
    paint_rectangle(x1=300, y1=50, x2=900, y2=450, color=2, width=3)
    # добовляем кирпичную стену
    wl.wall_draw(start_brick=300, end_brick=900, start_width_brick=50, end_width_brick=450, color_brick=colors[0][1])
    # рисуем окно дома
    paint_rectangle(x1=448, y1=198, x2=752, y2=402, color=0, width=0)
    # рисуем окно дома второй раз
    paint_rectangle(x1=450, y1=200, x2=750, y2=400, color=16, width=0)
    # рисуем крышу
    sd.start_drawing()
    for x in range(1, 100):
        roof_1 = sd.get_point(285+x, 451)
        roof_2 = sd.get_point(595, 550-x)
        roof_3 = sd.get_point(915-x, 451)
        sd.lines((roof_1, roof_2, roof_3), color=colors[11][1], closed=True, width=2)
    sd.finish_drawing()


# home_window_roof()

