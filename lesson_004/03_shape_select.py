# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
# TODO аналогично нейминг
# TODO Примерно новый объект данных может выглядеть вот так:
# TODO colors = {0: ['треугольник', функция_треугольник], 1: ['квадрат', функция_квадрат], и так далее!
shape_ls = [['треугольник', 120], ['квадрат', 90], ['пятиугольник', 72], ['шестиугольник', 60]]

print(f"Возможные варианты: ")
for index, value in enumerate(shape_ls):
    print(f"{index}: {value[0]}")

while True:
    user_input = input(f"Выбирите что нарисовать: ")
    if user_input.isdigit() and int(user_input) <= len(shape_ls) - 1:
        # colors_key = colors_list[int(user_input)]
        user_shape = shape_ls[int(user_input)][1]
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
    angle_triangle = user_shape
    draw_shape(point_start, ange_tilt, length_side, angle_triangle, color_shape=user_color)


def paint_square(point_start, ange_tilt, length_side):  # рисуем квадрат
    angle_square = user_shape
    draw_shape(point_start, ange_tilt, length_side, angle_square, color_shape=user_color)


def paint_pentagone(point_start, ange_tilt, length_side):  # рисуем пятиугольник
    angle_pentagone = user_shape
    draw_shape(point_start, ange_tilt, length_side, angle_pentagone, color_shape=user_color)


def paint_hexagon(point_start, ange_tilt, length_side):  # рисуем шестиугольник
    angle_hexagon = user_shape
    draw_shape(point_start, ange_tilt, length_side, angle_hexagon, color_shape=user_color)


user_color = sd.COLOR_DARK_YELLOW
initial_point = sd.get_point(300, 300)
# TODO тогда тут если мы по ключу выберем нужную нам функцию! Важно! не ее название, а именно функцию.
# TODO то нам останется подставить нужные параметры и вызвать ее тут используя ()
# TODO тогда не придется писать такую вложенность!
if user_shape == shape_ls[0][1]:
    paint_triangle(point_start=initial_point, ange_tilt=0, length_side=150)
elif user_shape == shape_ls[1][1]:
    paint_square(point_start=initial_point, ange_tilt=0, length_side=100)
elif user_shape == shape_ls[2][1]:
    paint_pentagone(point_start=initial_point, ange_tilt=0, length_side=100)
elif user_shape == shape_ls[3][1]:
    paint_hexagon(point_start=initial_point, ange_tilt=0, length_side=100)


sd.pause()
