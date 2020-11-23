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
        if self.house is not None:
            # TODO разве это хороший тон в нутри класса обращаться к другому класу?
            cat.house = self.house
            self.house.cat = cat
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
        # TODO по идеи если он умер, значит нам нужно удалить экземпляр класа кот!? Или он сам очистится?
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


my_cat = Cat(name_cat="Повелитель грязи")
my_sweet_home = House()


for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

random_man = randint(0, len(citizens) - 1)
citizens[random_man].pick_up_cat(cat=my_cat, )

for day in range(366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        # TODO переменная test была для отладки, хотел отловить момент когда кто то выполняет действие, у меня в
        #  процессе бывало так что в какой то день из 3х человек кто то один проподал и ничего не делал, но
        #  это не удачный код для этого
        #  вот пример http://joxi.ru/KAx0WRliKBJQMA
        citisen.act()
    my_cat.action_cat()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(my_cat)
    print(my_sweet_home)
    if my_cat.die() or citisen.die_man():  # проверка на жизнь
        break


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
