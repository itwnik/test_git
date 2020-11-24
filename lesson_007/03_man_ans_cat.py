# -*- coding: utf-8 -*-

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from random import randint
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness, )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            self.fullness -= 10
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    #  ------------Cat action---------
    def pick_up_cat(self, cat, ):
        # TODO можно упростить до if self.house:
        if self.house is not None:
            # TODO В данном случае мы на вход приняли экземпляр класса кот, и сним работаем в рамках метода
            cat.house = self.house
            # TODO что у вас происходит вот в этой сроке ? У дома не может быть новый параметра кот
            self.house.cat = cat
            # TODO можно обратиться к его имени cat.name
            cprint('{} подобрал кота и назвал его "{}"'.format(
                self.name, self.house.cat.name), color='red')

    def buy_food_cat(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.food_cat += 50
            cprint('{} сходил в магазин за едой коту по имени "{}"'.format(
                self.name, self.house.cat.name), color='red')
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_after_cat(self):
        # TODO если до 100 то тоже информировать и чистить до 0
        if self.house.dirt >= 100:
            self.fullness -= 20
            self.house.dirt -= 100
            cprint('{} убрал за котом по имени "{}" В доме чисто!'.format(
                self.name, self.house.cat.name), color='red')
    #  ------------

    def die_man(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return True

    def act(self):
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.food_cat < 50:
            self.buy_food_cat()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 4:
            self.clean_after_cat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.food_cat = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме человечей еды осталось {}, кошачей еды осталось {}, денег осталось {}, грязи {}'.format(
            self.food, self.food_cat, self.money, self.dirt, )


class Cat:

    def __init__(self, name_cat):
        self.name = name_cat
        self.fullness_cat = 0
        self.house = None

    def sleep_cat(self):
        self.fullness_cat -= 1
        cprint('Кот по имени "{}" поспал'.format(self.name), color='red')

    def eat_cat(self):
        if self.house.food_cat >= 10:
            self.fullness_cat += 20
            self.house.food_cat -= 10
            cprint('Кот по имени "{}" поел'.format(self.name), color='red')
        else:
            cprint('В доме кончелась еда для кота', color='red')

    def cat_dirt_generation(self):
        self.fullness_cat -= 10
        self.house.dirt += 100
        cprint('Кот по имени "{}" подрал обои, проклятый клубок шерсти'.format(self.name), color='red')

    def die(self):
        # TODO нет, удалять ничего не нужно просто у нас остановиться цикл и все
        if self.fullness_cat <= 0:
            cprint('Кот по имени "{}" умер...жаль...'.format(self.name), color='red')
            return True

    def action_cat(self):
        dice = randint(1, 6)
        if self.fullness_cat <= 50:
            self.eat_cat()
        elif self.house.dirt <= 10:
            self.cat_dirt_generation()
        elif dice == 4:
            self.eat_cat()
        elif dice == 3:
            self.cat_dirt_generation()
        else:
            self.sleep_cat()

    def __str__(self):
        return 'А шерстяному мешку какашек по имени "{}" на все пофиг, у него сытость {}'.format(
            self.name, self.fullness_cat, )


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'), ]

cats = [
    Cat(name_cat='Повелитель грязи'),
    Cat(name_cat='Шерстяной упырь'),
    Cat(name_cat='Милый говнюк'), ]

# my_cat = Cat(name_cat="Повелитель грязи")
my_sweet_home = House()


for citisen in citizens:
    index = citizens.index(citisen)
    citisen.go_to_the_house(house=my_sweet_home)
    citisen.pick_up_cat(cat=cats[index])

for day in range(366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        # TODO попадал скорее из за того что в некоторых методах нет принта если параметры не подошли под действие
        citisen.act()
    for my_cat in cats:
        my_cat.action_cat()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for my_cat in cats:
        print(my_cat)
    print(my_sweet_home)
    # TODO вот тут что то не так переменные не определены, + у вас же много жильцов а тут явно проверка только одного
    # TODO Нужно тольже делать цикл и там их чекать, но сделать так чтобы break выходил из главного цикла.
    if my_cat.die() or citisen.die_man():  # проверка на жизнь
        break

# TODO выживать они должны стабильно примерно 70 на 30%

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# TODO Имелось ввиду что если с тремя они не выживают в списке нужно оставить 2 кота, чтоб была стабильность
# (Можно определить критическое количество котов, которое может прокормить человек...)
