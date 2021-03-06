# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем (вывод на консоль и запрос ввода от пользователя) делать в 01_mastermind.py.
# Движок игры реализует только саму функциональность игры. Разделяем: mastermind_engine работает
# только с загаданным числом, а 01_mastermind - с пользователем и просто передает числа на проверку движку.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

#

"""

Игра «Быки и коровы»
Правила:
Компьютер загадывает четырехзначное число, все цифры которого различны
(первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
Игрок вводит четырехзначное число c неповторяющимися цифрами,
компьютер сообщают о количестве «быков» и «коров» в названном числе
«бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
      что и в задуманном числе
«корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
      что и в задуманном числе

Например, если задумано число 3275 и названо число 1234,
получаем в названном числе одного «быка» и одну «корову».
Очевидно, что число отгадано в том случае, если имеем 4 «быка».

"""

from mastermind_engine import mystery_number, end_game, check_input_number, check_bulls_crow
import termcolor as tc

count = 1
answer = {"bulls": 0, "crows": 0}


def input_and_check(text):
    while True:
        user_input = input(tc.colored(text, 'green', ))
        if check_input_number(user_input):
            return user_input
        print(f"Ошибка! повторите ввод!")


def check_user_answer_question(text):
    while True:
        user_input = input(tc.colored(text, 'green', ))
        if user_input == "y" or user_input == "n":
            break
        print(f"Ошибка! повторите ввод!")
    return user_input


def new_game():
    print("Игра «Быки и коровы»!")
    if check_user_answer_question("Распечатать правила? (y/n):") == "y":
        print(__doc__)
    tc.cprint("Игра началась!", 'red')
    # mystery_number()
    print(mystery_number())
    print("Компьютер загадал число XXXX")


def win_repeat(laps):
    global answer
    print(f"You WIN!!! Тебе понадобилось {laps - 1} раунда")
    if check_user_answer_question('Еще раз? (y/n): ') == "y":
        answer['bulls'] = 0
        new_game()
    else:
        print("Goodbye!!!!")


new_game()
while answer['bulls'] != 4:
    user_input_number = input_and_check(f"Отгадайте число которое загадал компьютер. Раунд № {count}: ")
    answer = check_bulls_crow(user_input_number)
    print(f"Быки - {answer['bulls']}, коровы - {answer['crows']}")
    count += 1
    if end_game(user_input_number):
        win_repeat(count)
        count = 1

# зачет!
