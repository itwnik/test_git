# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

user_color = sd.COLOR_GREEN
initial_point = sd.get_point(300, 300)


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


shapes = {0: ['треугольник', paint_triangle],
          1: ['квадрат', paint_square],
          2: ['пятиугольник', paint_pentagone],
          3: ['шестиугольник', paint_hexagon]}

print(f"Возможные варианты: ")
for index, value in shapes.items():
    print(f"{index}: {value[0]}")

while True:
    user_input = input(f"Выбирите что нарисовать: ")
    if user_input.isdigit() and int(user_input) in shapes.keys():
        user_shape = shapes[int(user_input)][1]
        break
    else:
        print(f"Ошибка! повторите ввод!")

# благодарю за подсказки, действительно, ткак круче, НО я не опнял следующие моменты
#  1. как сделать, чтоб окно рисвания вываливалоь на передний план?
# ответ, скорее это особенность системы на linuх все норм, а на виндов нет, затестил!
#  2. что объявляется первым, функция или переменнаяь(судя по данному заданию - функция)
# ответ, да все верно тут функция по скольку мы ее используем в словаре! Итерпритатор должен знать что
# такая функция есть в коде.
#  3. было ли в уроках рассказно как вызывать функцию из словаря? голову сломал покак гуглил)
# ответ, говорилось что при вызове () функция будет выполнять, о том как использовать функцию без () нет!
# часть обучения подразумевает как раз поиск информации из других источников! И так будет всегда)
# не только на курсе обучения.

user_shape(point_start=initial_point, ange_tilt=0, length_side=150)

sd.pause()

# зачет!
