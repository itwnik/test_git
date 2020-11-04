# -*- coding: utf-8 -*-


"""

Движок игры «Быки и коровы»

"""

import random as r

# TODO нужно если тип указать без ()
_num_string = str()


def mystery_number():
    # TODO Можно упростить заводим бесконечный цикл
    # TODO final_result присваиваем строку в которой randint(1000, 9999)
    # TODO Потом проверяем если set этой строки без дублей, (и прочекать длину)
    # TODO то выходим из цикла
    # TODO и возвращаем нужный нам результат
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

# TODO вот тут как раз пишем функцию проверки которая наружу будет выдавать True\False
# TODO нам нужен отдельный метод который чекает число пользователя на ошибки,
# TODO Можно создать список булевых значений и чекать его сразу в if функцией all, будет один if!
# TODO У вас должно быть 4 проверки: на число, на длинну, на длинну set, и на первый 0, только в нужном порядке!


def check_number(user_input):
    bulls_crow = {"bulls": 0, "crows": 0}
    for i in range(0, len(user_input)):
        if user_input[i] == _num_string[i]:
            bulls_crow["bulls"] += 1
        # TODO за место find можно использовать .count()
        elif user_input.find(_num_string[i]) >= 0:
            bulls_crow["crows"] += 1
    return bulls_crow


def end_game(is_game):
    # TODO можно сразу записать вот так
    # TODO return is_game == _num_string
    end = False
    if is_game == _num_string:
        end = True
    return end

