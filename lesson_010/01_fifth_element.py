# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42


def five_element():
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')


flag = 0
while flag == 0:
    try:
        five_element()
        flag = 1
    except IndexError as exc:
        print(f"невозможно преобразовать к числу: {exc}")
    except ValueError as exc:
        print(f"выход за границы списка: {exc}")
    except Exception as exc:
        print(f"неожиданная ошибка: {exc}")
print('Вам удалось ввести корректные данные! Ура!')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение
