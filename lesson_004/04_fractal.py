# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO part one
# initial_point = sd.get_point(300, 0)
#
#
# def draw_branches(start_point, angle_draw, length_branch):
#     vector_one = sd.get_vector(start_point=start_point, angle=angle_draw, length=length_branch)
#     vector_one.draw()
#     next_point = vector_one.end_point
#     vector_two = sd.get_vector(start_point=next_point, angle=angle_draw - 30, length=length_branch)
#     vector_two.draw()
#     vector_three = sd.get_vector(start_point=next_point, angle=angle_draw + 30, length=length_branch)
#     vector_three.draw()
#     return None
#
#
# draw_branches(start_point=initial_point, angle_draw=90, length_branch=150)

# TODO part two
# initial_point = sd.get_point(300, 0)
# sd.resolution = (1200, 600)
#
#
# def draw_branches(start_point, angle_draw, length_branch, ):
#     if length_branch < 4:  # проверяка на вход из рекурсии
#         return
#     # рисуем ствол
#     vector_one = sd.get_vector(start_point=start_point, angle=angle_draw, length=length_branch, )
#     vector_one.draw()
#     next_point = vector_one.end_point  # определяем следующую точку рисования ветки
#     r_next_angle_draw = angle_draw - 30  # определяем следующий угол рисования правой ветки
#     l_next_angle_draw = angle_draw + 30  # определяем следующий угол рисования левой ветки
#     next_length_branch = length_branch * .75  # # определяем следующий длину рисования ветки
#     # рисуем ветку
#     draw_branches(start_point=next_point, angle_draw=r_next_angle_draw, length_branch=next_length_branch, )  # правую
#     draw_branches(start_point=next_point, angle_draw=l_next_angle_draw, length_branch=next_length_branch, )  # левую
#     return vector_one.end_point
#
#
# # run from part 2 a task
# # draw_branches(start_point=initial_point, angle_draw=90, length_branch=150)
#
# TODO part three
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle_draw=90, length_branch=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()


# TODO part four

initial_point = sd.get_point(300, 0)
sd.resolution = (1200, 600)


def draw_branches(start_point, angle_draw, length_branch, ):
    if length_branch < 4:  # проверяка на вход из рекурсии
        return
    # рисуем ствол
    vector_one = sd.get_vector(start_point=start_point, angle=angle_draw, length=length_branch, )
    vector_one.draw()
    next_point = vector_one.end_point  # определяем следующую точку рисования ветки
    # определяем рандомную начальную и конечную точку угла в пределах 40% от 30 градусов
    random_tilt_start = int(30 * 1.4)
    random_tilt_end = int(30 * 0.6)
    # определяем следующий угол рисования правой ветки с учетом рандома
    r_next_angle_draw = angle_draw - sd.random_number(a=random_tilt_end, b=random_tilt_start)
    # определяем следующий угол рисования левой ветки с учетом рандома
    l_next_angle_draw = angle_draw + sd.random_number(a=random_tilt_end, b=random_tilt_start)
    # определяем рандомную начальную и конечную длину в пределах 20% от .75
    random_length_start = int(75 * 1.2)
    random_length_end = int(75 * .8)
    # определяем следующий длину рисования ветки с учетом рандома
    next_length_branch = length_branch * (sd.random_number(a=random_length_end, b=random_length_start) / 100)
    # рисуем ветку
    draw_branches(start_point=next_point, angle_draw=r_next_angle_draw, length_branch=next_length_branch, )  # правую
    draw_branches(start_point=next_point, angle_draw=l_next_angle_draw, length_branch=next_length_branch, )  # левую
    return vector_one.end_point


root_point = sd.get_point(300, 30)
draw_branches(start_point=root_point, angle_draw=90, length_branch=100)


sd.pause()
