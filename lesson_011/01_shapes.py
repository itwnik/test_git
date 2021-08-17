# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_shape(current_point_shape, ange_tilt, length_side, ):
        point_start = current_point_shape
        angle_draw_shape = int(360/n)
        for angle_shape in range(0, 360 - angle_draw_shape, angle_draw_shape):
            vector_shape = sd.get_vector(start_point=current_point_shape,
                                         angle=angle_shape + ange_tilt, length=length_side, width=2)
            vector_shape.draw()
            current_point_shape = vector_shape.end_point
        sd.line(current_point_shape, point_start, color=sd.COLOR_YELLOW, width=2)
    return draw_shape


draw_triangle = get_polygon(n=8)
draw_triangle(current_point_shape=sd.get_point(200, 200), ange_tilt=13, length_side=100)

sd.pause()

# зачет!
