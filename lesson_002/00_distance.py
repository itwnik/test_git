#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = dict()

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

# в питоне принято переменные называть в формате snake_case_one
# TODO немного не понял, можно пожалуйста пример? у меня вроде читаемое название переменной
# так нужно было назвать?  Moscow_London_case или  distance_Moscow_London_case
distance_Moscow_London = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** .5
distance_Moscow_Paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** .5
distance_London_Paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5

# distances = {'distance_Moscow_London': distance_Moscow_London,
#             'distance_Moscow_Paris': distance_Moscow_Paris,
#             'distance_London_Paris': distance_London_Paris}

distances['Moscow'] = {}
distances['Moscow']['London'] = distance_Moscow_London
distances['Moscow']['Paris'] = distance_Moscow_Paris

distances['London'] = {}
distances['London']['Moscow'] = distance_Moscow_London
distances['London']['Paris'] = distance_London_Paris

distances['Paris'] = {}
distances['Paris']['Moscow'] = distance_Moscow_Paris
distances['Paris']['London'] = distance_London_Paris

pprint(distances)