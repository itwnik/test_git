# -*- coding: utf-8 -*-


"""

Движок игры «Быки и коровы»

"""

import random as r

_num_string = str()


def mystery_number():  # TODO хотел через множества, но не догадался как изменить последоватьность, когда 0 первый
    global _num_string
    numbers = list()
    while len(numbers) < 4:
        temp = r.randint(0, 9)
        if temp not in numbers:
            if len(numbers) == 0 and temp == 0:
                pass
            else:
                numbers.append(temp)
    _num_string = ''.join(str(_num_string) for _num_string in numbers)
    return _num_string


def check_number(user_input):
    bulls_crow = {"bulls": 0, "crows": 0}
    for i in range(0, len(user_input)):
        if user_input[i] == _num_string[i]:
            bulls_crow["bulls"] += 1
        elif user_input.find(_num_string[i]) >= 0:
            bulls_crow["crows"] += 1
    return bulls_crow


def end_game(is_game):
    end = False
    if is_game == _num_string:
        end = True
    return end

