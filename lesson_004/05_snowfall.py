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


# sd.resolution = (1200, 600)
# settings_snowflake = []
# for _ in range(N):
#     x = sd.random_number(100, 1200)
#     y = sd.random_number(500, 600)
#     length = sd.random_number(20, 40)
#     settings_snowflake.append([x, y, length])

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
#   навсегда
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

sd.resolution = (1200, 600)
settings_snowflake = []
fallen_snow = []
for _ in range(N):
    x = sd.random_number(100, 1200)
    y = sd.random_number(500, 600)
    length = sd.random_number(20, 40)
    settings_snowflake.append([x, y, length])

# Выполнение задачи по Вашему алгоритму, как

# while True:
#     sd.clear_screen()
#     # sd.start_drawing()
#     for index in range(N):
#         point_x = settings_snowflake[index][0]
#         point_y = settings_snowflake[index][1]
#         center_snowflake = sd.get_point(settings_snowflake[index][0], settings_snowflake[index][1])  # рисуем снежинку
#         settings_snowflake[index][0] += sd.random_number(-15, 15)  # рандомное отклонение вправо/влево
#         settings_snowflake[index][1] -= sd.random_number(15, 25)
#         print(settings_snowflake)
#         sd.snowflake(center=center_snowflake, length=settings_snowflake[index][2])
#         if point_y < 50:  # если снежинка упала вниз
#             settings_snowflake[index][1] = 600  # начинаем снегопад заново
#             fallen_snow.append([point_x, point_y, settings_snowflake[index][2]])  # добовляем координаты ее в список
#         for index_1 in range(len(fallen_snow)):  # отрисовываем каждую упавшую снежинку из списка
#             center_fallen_snow = sd.get_point(fallen_snow[index_1][0], fallen_snow[index_1][1])
#             sd.snowflake(center=center_fallen_snow, length=settings_snowflake[index][2])
#     # sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():  # проверка выхода из цикла
#         break

# второй вариант, выдуманный мной.


while True:
    sd.start_drawing()
    for index in range(N):
        # TODO тут мы объявили point_x point_y, нужно еще и length
        point_x = settings_snowflake[index][0]
        point_y = settings_snowflake[index][1]
        # TODO вот тут в качестве аргументов как раз и передаем point_x point_y, length
        center_snowflake = sd.get_point(settings_snowflake[index][0], settings_snowflake[index][1])  # координаты
        # TODO тут мы печатаем sd.snowflake(... color=sd.background_color)
        # TODO это переносим в конец цикла
        if point_y < 50:
            settings_snowflake[index][1] = 600
        # TODO эту часть else убираем
        else:
            sd.snowflake(center=center_snowflake, length=settings_snowflake[index][2], color=sd.background_color)
        # TODO аналогично изменяем point_x point_y а не сразу в списке!
        settings_snowflake[index][0] += sd.random_number(-15, 15)
        settings_snowflake[index][1] -= sd.random_number(15, 25)
        # TODO в качестве аргументов передаем point_x point_y, length
        center_snowflake = sd.get_point(settings_snowflake[index][0], settings_snowflake[index][1])  # координаты
        sd.snowflake(center=center_snowflake, length=settings_snowflake[index][2])
        # TODO и после того как отрисовали мы сохраняем point_x point_y, length в нужную ячейку в список списков
        sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():  # проверка выхода из цикла
        break

sd.pause()

# TODO сугроб доработаем иным способом потому что создания нового списка через 5-10 мин будет тормозить программу!
# TODO сделаем point_y < 50:  число 50 вынесем в переменную
#  и сделаем динамическим изменяемым и на каждой итерации будем прибавлять +=0.5 или 1

