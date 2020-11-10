# -*- coding: utf-8 -*-

"""  Движок игры «Быки и коровы»  """

import random as r

_num_string = str()


def mystery_number():
    global _num_string
    while True:
        _num_string = str(r.randint(1000, 9999))
        if len(set(_num_string)) == 4:
            break
    return _num_string

# TODO чет я запутался с этими списками и функцией all()
#  кстати, ТУДУ можно не писать в каждой строке, пайчарм (версия 2020.2.1) понимает что ТУДУ продолжается
#  если сделать один пробел от начального ТУДУ ))


def check_input_number(user_input):
    correct = [user_input.isdigit() and int(user_input) > 0 and len(set(user_input)) == 4 and len(user_input) == 4]
    if all(correct):
        return True


def check_bulls_crow(user_input):
    bulls_crow = {"bulls": 0, "crows": 0}
    for i in range(len(user_input)):
        if user_input[i] == _num_string[i]:
            bulls_crow["bulls"] += 1
        elif user_input.find(_num_string[i]) >= 0:
            bulls_crow["crows"] += 1
    return bulls_crow


def end_game(is_game):
    return is_game == _num_string

