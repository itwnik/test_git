# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:
    def __init__(self):
        self.element = "Вода"

    def __add__(self, other):
        if other.element == "Огонь":
            new_obj = Steam()
        elif other.element == "Воздух":
            new_obj = Storm()
        elif other.element == "Земля":
            new_obj = Dirt()
        elif other.element == "Голова":
            new_obj = SecretElement1()
        else:
            new_obj = None
        return new_obj

    def __str__(self):
        return f"{self.element}"


class Air:
    def __init__(self):
        self.element = "Воздух"

    def __add__(self, other):
        if other.element == "Огонь":
            new_obj = Lightning()
        elif other.element == "Вода":
            new_obj = Storm()
        elif other.element == "Земля":
            new_obj = Dust()
        elif other.element == "Голова":
            new_obj = SecretElement1()
        else:
            new_obj = None
        return new_obj

    def __str__(self):
        return f"{self.element}"


class Earth:
    def __init__(self):
        self.element = "Земля"

    def __add__(self, other):
        if other.element == "Огонь":
            new_obj = Lava()
        elif other.element == "Вода":
            new_obj = Dirt()
        elif other.element == "Воздух":
            new_obj = Dust()
        elif other.element == "Голова":
            new_obj = SecretElement3()
        else:
            new_obj = None
        return new_obj

    def __str__(self):
        return f"{self.element}"


class Fire:
    def __init__(self):
        self.element = "Огонь"

    def __add__(self, other):
        if other.element == "Земля":
            new_obj = Lava()
        elif other.element == "Воздух":
            new_obj = Lightning()
        elif other.element == "Вода":
            new_obj = Steam()
        elif other.element == "Голова":
            new_obj = SecretElement4()
        else:
            new_obj = None
        return new_obj

    def __str__(self):
        return f"{self.element}"


class Steam:
    def __init__(self):
        self.element = "Пар"

    def __str__(self):
        return f"{self.element}"


class Storm:
    def __init__(self):
        self.element = "Шторм"

    def __str__(self):
        return f"{self.element}"


class Dirt:
    def __init__(self):
        self.element = "Грязь"

    def __str__(self):
        return f"{self.element}"


class Lightning:
    def __init__(self):
        self.element = "Молния"

    def __str__(self):
        return f"{self.element}"


class Dust:
    def __init__(self):
        self.element = "Пыль"

    def __str__(self):
        return f"{self.element}"


class Lava:
    def __init__(self):
        self.element = "Лава"

    def __str__(self):
        return f"{self.element}"


class Head:
    def __init__(self):
        self.element = "Голова"  # имеются ввиду волосы которые на голове

    def __add__(self, other):
        if other.element == "Вода":
            new_obj = SecretElement1()
        elif other.element == "Воздух":
            new_obj = SecretElement2()
        elif other.element == "Земля":
            new_obj = SecretElement3()
        elif other.element == "Огонь":
            new_obj = SecretElement4()
        else:
            new_obj = None
        return new_obj

    def __str__(self):
        return f"{self.element}"


class SecretElement1:  # +ВОДА
    def __init__(self):
        self.element = "Мокрая голова"

    def __str__(self):
        return f"{self.element}"


class SecretElement2:  # +Воздух
    def __init__(self):
        self.element = "Сухая голова"

    def __str__(self):
        return f"{self.element}"


class SecretElement3:  # +Земля
    def __init__(self):
        self.element = "Грязная голова"

    def __str__(self):
        return f"{self.element}"


class SecretElement4:  # +Огонь
    def __init__(self):
        self.element = "Стрижка горячими ножницами"

    def __str__(self):
        return f"{self.element}"


water_element = Water()
air_element = Air()
earth_element = Earth()
fire_element = Fire()
head_element = Head()

elements = [water_element, air_element, earth_element, fire_element]


def user_inputs(element_number):
    while True:
        print(f"Выбирите номер {element_number} элемента ")
        user_input = input(f"{', '.join(str(elements.index(elem)) + str(' : ') + str(elem) for elem in elements)}: ")
        if user_input.isdigit() and int(user_input) <= len(elements)-1:
            return user_input
        print(f"Ошибка! повторите ввод!")


def user_inputs_y_n(text):
    while True:
        user_input = input(f"{text} (y/n): ")
        if user_input == "y" or user_input == "n":
            return user_input
        print(f"Ошибка! повторите ввод!")


repeat = "y"
while repeat == "y":
    # TODO secret переменная не объявлена!
    if head_element in elements and secret == 0:
        elements.remove(head_element)
    element_1 = int(user_inputs("первого"))
    element_2 = int(user_inputs("второго"))
    print(f"{str(elements[element_1])} + {str(elements[element_2])} = {elements[element_1] + elements[element_2]}")
    if user_inputs_y_n("Повторить игру?") == "y":
        repeat = "y"
        if user_inputs_y_n("ввести в игру секретный элемент =) ?") == "y":
            secret = 1
            elements.append(head_element)
        else:
            secret = 0
    else:
        repeat = "n"

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
