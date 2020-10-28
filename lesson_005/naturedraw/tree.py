# -*- coding: utf-8 -*-

import simple_draw as sd

# TODO поиграйтесь можно попробовать с старт и ент дравфтинг поиграться


def draw_branches(start_point, angle_draw, length_branch, color=sd.COLOR_YELLOW):
    if length_branch < 5:  # проверяка на вход из рекурсии
        return
    # рисуем ствол

    vector_one = sd.get_vector(start_point=start_point, angle=angle_draw, length=length_branch, )
    sd.start_drawing()
    vector_one.draw(color=color)
    sd.finish_drawing()
    next_point = vector_one.end_point  # определяем следующую точку рисования ветки
    # определяем рандомную начальную и конечную точку угла в пределах 40% от 30 градусов
    random_tilt_start = int(30 * 1.4)
    random_tilt_end = int(30 * 0.6)
    # определяем следующий угол рисования правой ветки с учетом рандома
    r_next_angle_draw = angle_draw - sd.random_number(a=random_tilt_end, b=random_tilt_start)
    # определяем следующий угол рисования левой ветки с учетом рандома
    l_next_angle_draw = angle_draw + sd.random_number(a=random_tilt_end, b=random_tilt_start)
    # определяем рандомную начальную и конечную длину в пределах 20% от .75
    random_length_start = int(75 * 1.15)
    random_length_end = int(75 * .8)
    # определяем следующий длину рисования ветки с учетом рандома
    next_length_branch = length_branch * (sd.random_number(a=random_length_end, b=random_length_start) / 100)
    if next_length_branch < 20:
        color = sd.COLOR_GREEN
    sd.start_drawing()
    # рисуем ветку
    draw_branches(start_point=next_point, angle_draw=r_next_angle_draw, length_branch=next_length_branch, color=color)  # правую
    sd.finish_drawing()
    draw_branches(start_point=next_point, angle_draw=l_next_angle_draw, length_branch=next_length_branch, color=color)  # левую

    return vector_one.end_point


# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle_draw=90, length_branch=100)
