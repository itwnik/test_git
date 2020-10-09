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

# TODO тут тоже можно что то оптимизировать?
#   не пойму, почему у меня после ввода не переходит на первый план окно рисования!?
print(f"Сейчас будут нарисованы 4 фигуры: треугольник, квадрат, пятиугольник, шестиугольник!")

# TODO Примерно новый объект данных может выглядеть вот так:
# TODO colors = {0: ['red', sd.COLOR_RED], 1: ['orange', sd.COLOR_ORANGE], и так далее! 
# TODO По ключу мы сразу будем получать список нужных нам данных и уже ими оперировать в коде через индекс!

# TODO цветов должно быть больше! + объединить с colors_ls, нейминг dic и ls в названии только все утают их понимание
colors_dic = {"red": sd.COLOR_RED,
              "orange": sd.COLOR_ORANGE,
              "yellow": sd.COLOR_YELLOW,
              }
colors_ls = ["red", "orange", "yellow"]

for index, value in enumerate(colors_ls):
    print(f"{index}: {value}")

while True:
    user_input = input(f"Выбирите цвет, которым будт нарисованы фигуры: ")
    # TODO вторым уловие можно будет проверить на вхождение в словарь
    if user_input.isdigit() and int(user_input) <= len(colors_dic) - 1:
        colors_key = colors_ls[int(user_input)]
        user_color = colors_dic[colors_key]
        break
    else:
        print(f"Ошибка! повторите ввод!")

# TODO функции объявляем до основной логики программы!
def draw_shape(current_point_shape, ange_tilt, length_side, angle_draw_shape, color_shape, ):
    point_start = current_point_shape
    for angle_shape in range(0, 360 - angle_draw_shape, angle_draw_shape):
        vector_shape = sd.get_vector(start_point=current_point_shape,
                                     angle=angle_shape+ange_tilt, length=length_side, width=3)
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


# TODO переменные объявляем до основной логики программы!
initial_point_triangle = sd.get_point(100, 100)
initial_point_square = sd.get_point(100, 300)
initial_point_pentagone = sd.get_point(400, 100)
initial_point_hexagon = sd.get_point(400, 300)

paint_triangle(point_start=initial_point_triangle, ange_tilt=15, length_side=150)
paint_square(point_start=initial_point_square, ange_tilt=25, length_side=100)
paint_pentagone(point_start=initial_point_pentagone, ange_tilt=30, length_side=100)
paint_hexagon(point_start=initial_point_hexagon, ange_tilt=10, length_side=100)

sd.pause()