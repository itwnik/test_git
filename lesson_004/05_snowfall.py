# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


sd.resolution = (1200, 600)
settings_snowflake = []
for _ in range(N):
    x = sd.random_number(100, 1200)
    y = sd.random_number(500, 600)
    length = sd.random_number(20, 40)
    settings_snowflake.append([x, y, length])

# while True:
#     sd.clear_screen()
#     for index in range(N):
#         point_x = settings_snowflake[index][0]
#         point_y = settings_snowflake[index][1]
#         center_snowflake = sd.get_point(settings_snowflake[index][0], settings_snowflake[index][1])  # рисуем снежинку
#         settings_snowflake[index][0] += 5
#         settings_snowflake[index][1] -= 20
#         sd.snowflake(center=center_snowflake, length=settings_snowflake[index][2])
#         if point_y < 50:
#             settings_snowflake[index][1] = 600

#         if point_x > 1100:  # доработал сдвиг по х тоже
#             settings_snowflake[index][0] = 50
#
#     sd.sleep(0.1)
#     if sd.user_want_exit():  # проверка выхода из цикла
#         break


# Примерный алгоритм отрисовки снежинок
#   навсегд а
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       изменить координата_у и запомнить её в списке по индексу
#       создать точку отрисовки снежинки по координатам
#       нарисовать снежинку белым цветом в этой точке
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# while True:
#     sd.start_drawing()
#     for index in range(N):
#         point_x = settings_snowflake[index][0]
#         point_y = settings_snowflake[index][1]
#         center_snowflake = sd.get_point(settings_snowflake[index][0], settings_snowflake[index][1])  # координаты
#         sd.snowflake(center=center_snowflake, length=settings_snowflake[index][2], color=sd.background_color)
#         settings_snowflake[index][0] += 5
#         settings_snowflake[index][1] -= 20
#         center_snowflake = sd.get_point(settings_snowflake[index][0], settings_snowflake[index][1])  # координаты
#         sd.snowflake(center=center_snowflake, length=settings_snowflake[index][2])
#         sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():  # проверка выхода из цикла
#         break


# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

# TODO доработать алгоритм из первой части без наворотов!
# TODO нужно только добавить рендомное отклонение без условий
# TODO и только одно условие в конце цикла фор на упавшею снежинку
while True:
    sd.start_drawing()
    for step, index in enumerate(range(N)):
        point_x = settings_snowflake[index][0]
        point_y = settings_snowflake[index][1]
        center_snowflake = sd.get_point(settings_snowflake[index][0], settings_snowflake[index][1])  # координаты
        if point_y <= settings_snowflake[index][2]:  # если снежинка в конце экране не закрашиваем ее цветом экрана
            settings_snowflake[index][1] = 600  # запускаем снегопад повторно
            #  index -= 1  # этот код добовляет +1 снежинку ксли я правильно понял
            pass
        else:
            sd.snowflake(center=center_snowflake, length=settings_snowflake[index][2], color=sd.background_color)
        if step % 2 == 0:  # рандомное отклонение вправо/влево
            settings_snowflake[index][0] += sd.random_number(5, 10)  # 5
        else:
            settings_snowflake[index][0] -= sd.random_number(10, 20)  # 15
        settings_snowflake[index][1] -= 15
        center_snowflake = sd.get_point(settings_snowflake[index][0], settings_snowflake[index][1])  # координаты
        sd.snowflake(center=center_snowflake, length=settings_snowflake[index][2])
        sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():  # проверка выхода из цикла
        break

sd.pause()

# TODO снегопад не должен заканчиваться !
