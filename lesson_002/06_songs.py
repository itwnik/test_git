#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
# Три песни звучат ХХХ.XX минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

#

# у нас значение в словарях в формате 4.86 - это и есть float преобразовывать не нужно
three_songs = round(violator_songs[3][1] + violator_songs[5][1] + violator_songs[8][1], 2)
print(f"Три песни звучат 0{three_songs} минут")

# Есть словарь песен группы Yellow со временем звучания с точностью до долей минут
pocket_universe_songs = {
    'Solar Driftwood': 1.85,
    'Celsius': 5.98,
    'More': 6.65,
    'On Track': 5.55,
    'Monolith': 6.35,
    'To the Sea': 5.77,
    'Magnetic': 5.88,
    'Liquid Mountain': 2.97,
    'Pan Blue': 5.52,
    'Resistor': 7.22,
    'Beyond Mirrors': 5.82,
}

# Распечатайте общее время звучания трех песен: 'On Track', 'To the Sea' и 'Beyond Mirrors'
#   А другие три песни звучат приблизительно ХХХ минут

#
#  Для переноса не используйте знак \, а лучше все всзять в () и перенести по математическому знаку,
#  или другому символу
Yellow_three_songs = (pocket_universe_songs['On Track'] + pocket_universe_songs['To the Sea'] +
                      pocket_universe_songs['Beyond Mirrors'])
#  Для переноса не используйте знак \, а лучше все всзять в () и перенести по математическому знаку,
#  или другому символу
other_three_songs = round(pocket_universe_songs['Solar Driftwood'] + pocket_universe_songs['Celsius'] +
                          pocket_universe_songs['Pan Blue'])
#  стараемся конкатенацию строк в принте не использовать, либо через (,)
#  самый новый формат для печати в принт это f - строки или более ранний .format()
#  преобразование к str делать не нужно принт и так распечатает!
print(f"Общее время звучания трех песен: On Track, To the Sea и Beyond Mirrors {Yellow_three_songs} минут")
print(f"А другие три песни звучат приблизительно 0{other_three_songs} минут")

# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# зачет!

