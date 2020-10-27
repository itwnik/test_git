# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)


import home as h
import naturedraw.rainbow as rb
import naturedraw.smile as sm
import naturedraw.tree as tr
import naturedraw.snow as sn
import simple_draw as sd


def sun_draw():  # функция рисования солнца
    sun_point = sd.get_point(400, 700)
    sd.circle(sun_point, width=0)
    for angle_sun_ray in range(0, 360, 30):
        # random_length = sd.random_number(60, 100)
        sd.start_drawing()
        sun_ray = sd.get_vector(sun_point, angle_sun_ray, length=100, width=3)
        sun_ray.draw()
        sd.finish_drawing()


def lend(x_land):  # функция рисования земли под домом
    left_bottom = sd.get_point(0, 0)
    right_top = sd.get_point(x_land, 50)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_DARK_CYAN, width=0)


sd.resolution = (1600, 800)

# рисуем солнце
sun_draw()
# рисуем землю под домом
lend(1600)
# рисуем радугу
rb.rainbow_draw()
# рисуем дом с крышей и окном
h.home_window_roof()
# рисуем смайл
sm.emoji(coord_x=600, coord_y=300, color=sd.COLOR_YELLOW)
# рисуем 3 дерева
root_point = sd.get_point(1180, 63)
tr.draw_branches(start_point=root_point, angle_draw=90, length_branch=100)
root_point = sd.get_point(1280, 450)
tr.draw_branches(start_point=root_point, angle_draw=95, length_branch=50)
root_point = sd.get_point(1080, 500)
tr.draw_branches(start_point=root_point, angle_draw=95, length_branch=50)
# рисуем снегопад
sn.snow()

sd.pause()
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
