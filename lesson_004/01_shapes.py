# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg
# sd.resolution = (1200, 800)

# TODO Хорошо у вас сейчас три параметра, точка, угол наклона, и длина
def paint_triangle(point_start, ange_tilt, length_side):  # рисуем треугольник
    current_point_shape = point_start
    # TODO тут мы заведем range от 0, до 360-120(чтобы крутить без крайнего вектора), с шагом 120
    for angle_shape in range(ange_tilt, 360 + ange_tilt, 120):
        # TODO а вот тут в параметре angle=angle_shape+ange_tilt
        vector_shape = sd.get_vector(start_point=current_point_shape,
                                     angle=angle_shape, length=length_side, width=2)
        vector_shape.draw()
        current_point_shape = vector_shape.end_point
    # TODO тогда мы просто без условий после цикла напечатаем sd.line крайнею линию
        if angle_shape == 120 + ange_tilt:
            sd.line(current_point_shape, point_start, color=sd.COLOR_YELLOW, width=2)
            break
    # TODO возвращать ничего не нужно, return None - такая конструкция абсурдная потому что возвращает None
    return None


initial_point_triangle = sd.get_point(300, 300)
paint_triangle(initial_point_triangle, ange_tilt=0, length_side=150)


def paint_square(point_start, ange_tilt, length_side):  # рисуем квадрат
    current_point_shape = point_start
    for angle_shape in range(ange_tilt, 360 + ange_tilt, 90):
        vector_shape = sd.get_vector(start_point=current_point_shape,
                                     angle=angle_shape, length=length_side, width=2)
        vector_shape.draw()
        current_point_shape = vector_shape.end_point
        if angle_shape == 180 + ange_tilt:
            sd.line(current_point_shape, point_start, color=sd.COLOR_YELLOW, width=2)
            break
    return None


initial_point_square = sd.get_point(100, 300)
paint_square(initial_point_square, ange_tilt=25, length_side=100)


def paint_pentagone(point_start, ange_tilt, length_side):  # рисуем пятиугольник
    current_point_shape = point_start
    for angle_shape in range(ange_tilt, 360 + ange_tilt, 72):
        vector_shape = sd.get_vector(start_point=current_point_shape,
                                     angle=angle_shape, length=length_side, width=2)
        vector_shape.draw()
        current_point_shape = vector_shape.end_point
        if angle_shape == 216 + ange_tilt:
            sd.line(current_point_shape, point_start, color=sd.COLOR_YELLOW, width=2)
            break
    return None


initial_point_pentagone = sd.get_point(100, 100)
paint_pentagone(initial_point_pentagone, ange_tilt=0, length_side=100)


def paint_hexagon(point_start, ange_tilt, length_side):  # рисуем шестиугольник
    current_point_shape = point_start
    for angle_shape in range(ange_tilt, 360 + ange_tilt, 60):
        vector_shape = sd.get_vector(start_point=current_point_shape,
                                     angle=angle_shape, length=length_side, width=2)
        vector_shape.draw()
        current_point_shape = vector_shape.end_point
        if angle_shape == 240 + ange_tilt:
            sd.line(current_point_shape, point_start, color=sd.COLOR_YELLOW, width=2)
            break
    return None


initial_point_hexagon = sd.get_point(400, 100)
paint_hexagon(initial_point_hexagon, ange_tilt=55, length_side=100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
