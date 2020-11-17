# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(50, 550)
        self.y = sd.random_number(550, 580)
        self.length = sd.random_number(20, 24)

    def move(self):
        # TODO используем метод can_fall, если может падать то изменяем
        self.x += sd.random_number(-15, 15)  # меняем х
        self.y -= sd.random_number(15, 25)  # меняем у

    def draw(self, snowflake_color):
        center_snowflake = sd.get_point(self.x, self.y)  # получаем центр снежинки
        sd.snowflake(center_snowflake, length=self.length, color=snowflake_color)  # рисуем синим снежинку

    def can_fall(self):
        # TODO можно упростить написав сразу так return self.y >= 30
        if self.y <= 30:
            return False
        else:
            return True

    def __str__(self):
        return 'Snowflake: ' + ', '.join(self.x) + ', '.join(self.y) + ', '.join(self.length)

#  ШАГ 1
# flake = Snowflake()
#
# while True:
#     flake.draw(snowflake_color=sd.background_color)
#     flake.move()
#     flake.draw(snowflake_color=sd.COLOR_WHITE)
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

#  ШАГ 2


def get_flakes(quantity):
    flakes_roster = []
    for _ in range(quantity):
        flakes_roster.append(Snowflake())
    return flakes_roster


def get_fallen_flakes():
    count = 0
    # TODO нейминг, старайтесь не сокращать называния
    for fl in flakes:
        if not fl.can_fall():
            count += 1
            fl.draw(snowflake_color=sd.background_color)  # TODO снежинки - удаляем!
            flakes.remove(fl)
    return count


def append_flakes(quantity):
    # как бы мы должны знать от куда у нас в функции flakes
    global flakes
    flakes.extend(get_flakes(quantity))


flakes = get_flakes(quantity=25)
while True:
    for flake in flakes:
        sd.start_drawing()
        flake.draw(snowflake_color=sd.background_color)
        flake.move()
        flake.draw(snowflake_color=sd.COLOR_WHITE)
        sd.finish_drawing()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(fallen_flakes)
        # print(len(flakes))
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
