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
        if self.house:
            cat.house = self.house
            cprint('{} подобрал кота и назвал его "{}"'.format(
                self.name, cat.name), color='red')

    def buy_food_cat(self, cat):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.food_cat += 50
            # TODO как в данном случае обратиться к коту? так?
            cprint('{} сходил в магазин за едой коту по имени "{}"'.format(
                self.name, cat.name), color='red')
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_after_cat(self, cat):
        if self.house.dirt > 0:
            while self.house.dirt > 100:  # Это по условиям задачи
                self.fullness -= 20
                self.house.dirt -= 100
            else:   # Это чтоб до 0
                self.fullness -= 20
                self.house.dirt -= self.house.dirt
            cprint('{} убрал за котом по имени "{}" В доме чисто!'.format(
                self.name, cat.name), color='red')
    #  ------------

    def die_man(self, day):
        if self.fullness <= 0:
            cprint('{} умер... на {} день'.format(self.name, day), color='red')
            return True

    def act(self, cat, ):
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.food_cat < 50:
            self.buy_food_cat(cat)
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 4:
            self.clean_after_cat(cat)
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
        self.house.dirt += 5
        cprint('Кот по имени "{}" подрал обои, проклятый клубок шерсти'.format(self.name), color='red')

    def die_cat(self, day, ):
        if self.fullness_cat <= 0:
            cprint('Кот по имени "{}" умер на {} день...жаль...'.format(self.name, day), color='red')
            return True

    def action_cat(self):
        dice = randint(1, 6)
        if self.fullness_cat <= 50:
            self.eat_cat()
        elif dice == 2:
            self.cat_dirt_generation()
        elif dice == 4:
            self.eat_cat()
        elif dice == 6:
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

my_sweet_home = House()

for citisen in citizens:
    index = citizens.index(citisen)
    citisen.go_to_the_house(house=my_sweet_home)
    citisen.pick_up_cat(cat=cats[index])
the_end = 1
for day in range(366):
    if the_end == 0:
        break
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        index = citizens.index(citisen)
        citisen.act(cat=cats[index])
    for my_cat in cats:
        my_cat.action_cat()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for my_cat in cats:
        print(my_cat)
    print(my_sweet_home)

    for man_cats in range(len(citizens)):
        if cats[man_cats].die_cat(day) or citizens[man_cats].die_man(day):
            the_end = 0

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# TODO Имелось ввиду что если с тремя они не выживают в списке нужно оставить 2 кота, чтоб была стабильность
# (Можно определить критическое количество котов, которое может прокормить человек...)
