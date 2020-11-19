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
        # TODO это убераем
        # self.cat = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness, )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            # TODO уменьшаем сытость
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

    #  ------------Cat action----------
    # TODO у человека не может быть параметра кот, и мы не создаем его тут!
    # TODO метод pick_up_cat лишь дает человеку возможность подобрать кота и назначить ему дом!
    # TODO так и нужно делать:
    #  например так  cat.house = self.house (только как раз с self) тогда уйдет строчка self.cat = cat

    # TODO тут мы принимаем только экземпляр класса cat
    def pick_up_cat(self, cat, house):
        # TODO сейчас это строка ругается на что нет такой переменной, но она нам и не нужна!
        self.cat = cat
        # TODO тут делаем проверку есть ли у человека дом, если да то этот дом присваиваем коту и тогда
        # TODO они будут жить в общем доме, если дома у человека нет то и кота он взять не может!
        self.cat.house = house
        # TODO часть этих методов у нас уже есть в доме, от сюда их убираем они не нужны!
        self.house.cat = cat
        self.house.food_cat = 100
        self.house.dirt = 150
        cprint('{} подобрал кота и назвал его "{}"'.format(self.name, self.house.cat.name), color='red')

    def buy_food_cat(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой коту по имени "{}"'.format(self.name, self.house.cat.name), color='red')
            self.house.money -= 50
            self.house.food_cat += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_after_cat(self):
        if self.house.dirt >= 100:
            cprint('{} убрал за котом по имени "{}"'.format(self.name, self.house.cat.name), color='red')
            self.fullness -= 20
            self.house.dirt -= 100
        # TODO информируем о том что в доме чисто
    #  ------------

    def act(self):
        # TODO вынесем это в отдельный метод и будем проверять в цикле в конце дня, после всех действий
        # TODO задача добиться чтобы цикл останавливался в случае чего!
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
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
        elif dice == 3:
            self.clean_after_cat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        # TODO эти параметры зададим по дефолту, думаю что человек давно искал кота
        # TODO но обнулим их
        # self.food_cat = 120
        self.money = 0
        # TODO грязь тоже как бы в доме есть
        # self.dirt = 0
        # TODO у дома не может быть параметра кот
        self.cat = None

    def __str__(self):
        return 'В доме человечей еды осталось {}, кошачей еды осталось {}, денег осталось {}, грязи {}'.format(
            self.food, self.food_cat, self.money, self.dirt, )


class Cat:

    def __init__(self, name_cat):
        self.name = name_cat
        self.fullness_cat = 50
        self.house = None

    def sleep_cat(self):
        cprint('Кот по имени "{}" поспал'.format(self.name), color='red')
        self.fullness_cat -= 10

    def eat_cat(self):
        # TODO делаем проверку на еду если есть то он есть если нет то информируем в консоле
        cprint('Кот по имени "{}" поел'.format(self.name), color='red')
        self.fullness_cat += 20
        self.house.food_cat -= 10

    def cat_dirt_generation(self):
        cprint('Кот по имени "{}" подрал обои, проклятый клубок шерсти'.format(self.name), color='red')
        self.fullness_cat -= 10
        self.house.dirt += 150

    def action_cat(self):
        # TODO вынесем в отдельный метод
        if self.fullness_cat <= 0:
            cprint('Кот по имени "{}" умер...жаль...'.format(self.name), color='red')
            return
        # TODO тут добавим рендомности и некоторые методы продублируем на волю случая
        if self.fullness_cat <= 50:
            self.eat_cat()
        elif self.house.dirt <= 10:
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
#
my_cat = Cat(name_cat="Повелитель грязи")
my_sweet_home = House()


for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

# TODO эту часть вынесете в отдельную переменную
#  randint(0, len(citizens) - 1)
citizens[randint(0, len(citizens) - 1)].pick_up_cat(cat=my_cat, house=my_sweet_home)

# можно так
for day in range(366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        # TODO зачем тут переменная test усложнение и лишняя переменная, + вложенность, от вложенности
        # TODO может быть и не уйдем в доработках но в данном моменте она не нужна.
        test = citisen.act()
        if test:
            print('test')
    my_cat.action_cat()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(my_cat)
    print(my_sweet_home)
    # TODO проверку на жизнь делать тут в конце цикла

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
