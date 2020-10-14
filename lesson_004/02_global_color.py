# -*- coding: utf-8 -*-
import simple_draw as sd

# import sys

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

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

initial_point_triangle = sd.get_point(100, 100)
initial_point_square = sd.get_point(100, 300)
initial_point_pentagone = sd.get_point(400, 100)
initial_point_hexagon = sd.get_point(400, 300)


def draw_shape(current_point_shape, ange_tilt, length_side, angle_draw_shape, color_shape, ):
    point_start = current_point_shape
    for angle_shape in range(0, 360 - angle_draw_shape, angle_draw_shape):
        vector_shape = sd.get_vector(start_point=current_point_shape,
                                     angle=angle_shape + ange_tilt, length=length_side, width=3)
        vector_shape.draw(color=color_shape)
        current_point_shape = vector_shape.end_point
    sd.line(current_point_shape, point_start, color=color_shape, width=3)


def paint_triangle(point_start, ange_tilt, length_side):  # рисуем треугольник
    angle_triangle = 120
    draw_shape(point_start, ange_tilt, length_side, angle_triangle, color_shape=user_color)


def paint_square(point_start, ange_tilt, length_side):  # рисуем квадрат
    angle_square = 90
    draw_shape(point_start, ange_tilt, length_side, angle_square, color_shape=user_color)


def paint_pentagone(point_start, ange_tilt, length_side):  # рисуем пятиугольник
    angle_pentagone = 72
    draw_shape(point_start, ange_tilt, length_side, angle_pentagone, color_shape=user_color)


def paint_hexagon(point_start, ange_tilt, length_side):  # рисуем шестиугольник
    angle_hexagon = 60
    draw_shape(point_start, ange_tilt, length_side, angle_hexagon, color_shape=user_color)


print(f"Сейчас будут нарисованы 4 фигуры: треугольник, квадрат, пятиугольник, шестиугольник!")

for key, value in colors.items():
    print(f"{key}: {value[0]} ")

while True:
    user_input = input(f"Выбирите цвет, которым будт нарисованы фигуры: ")
    if user_input.isdigit() and int(user_input) in colors.keys():
        user_color = colors[int(user_input)][1]
        break
    else:
        print(f"Ошибка! повторите ввод!")

paint_triangle(point_start=initial_point_triangle, ange_tilt=15, length_side=150)
paint_square(point_start=initial_point_square, ange_tilt=25, length_side=100)
paint_pentagone(point_start=initial_point_pentagone, ange_tilt=30, length_side=100)
paint_hexagon(point_start=initial_point_hexagon, ange_tilt=10, length_side=100)

sd.pause()

# зачет!
