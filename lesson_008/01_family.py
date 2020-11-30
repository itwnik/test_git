# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money_casket = 100
        self.eat_fridge = 50
        self.dirt_house = 0

    def dirt_generation(self):
        self.dirt_house += 5

    def __str__(self):
        return f"В доме денег {self.money_casket}, еды {self.eat_fridge}, грязи {self.dirt_house}"


class Human:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house

    def __str__(self):
        return f"{self.name} сытость {self.fullness}, счастье {self.happiness}"

    def eat(self):
        if self.house.eat_fridge > 30:
            self.fullness += 30
            self.house.eat_fridge -= 30
            cprint('{} поел'.format(self.name), color='green')
        else:
            self.fullness -= 10
            cprint('{}, в доме нет еды!'.format(self.name), color='red')

    def who_in_the_shit(self):
        if self.house.dirt_house >= 90:
            self.happiness -= 10

    def die(self):
        if self.fullness == 0 or self.happiness < 10:
            cprint('Персонаж {} умер...'.format(self.name), color='red')
            return True


class Husband(Human):

    # TODO нет необходимости этот метод переопределять!
    def __str__(self):
        return super().__str__()

    def act(self):
        magic_ball = randint(1, 8)
        if self.fullness < 40:
            self.eat()
        elif self.house.money_casket < 400:
            self.work()
        # TODO это оставим на волю случая, вызывать будем по magic_ball, у вас он уже есть
        elif self.happiness < 60:
            self.gaming()
        elif magic_ball == 1:
            self.gaming()
        elif magic_ball == 3:
            self.eat()
        elif magic_ball == 5:
            self.work()
        else:
            self.gaming()

    def work(self):
        self.fullness -= 10
        self.happiness -= 10
        self.house.money_casket += 150
        cprint('{} сходил на работу'.format(self.name), color='green')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        cprint('{} играл в WoT'.format(self.name), color='green')


class Wife(Human):

    # TODO аналогично, туду выше
    def __str__(self):
        return super().__str__()

    def act(self):
        magic_ball = randint(1, 8)
        if self.house.eat_fridge < 40:
            self.shopping()
        elif self.fullness < 30:
            self.eat()
        elif self.happiness < 70:
            self.buy_fur_coat()
        # TODO это оставим на волю случая
        elif self.house.dirt_house > 50:
            self.clean_house()
        elif magic_ball == 2:
            self.buy_fur_coat()
        elif magic_ball == 4:
            self.shopping()
        elif magic_ball == 6:
            self.clean_house()
        else:
            self.buy_fur_coat()

    def shopping(self):
        if self.house.money_casket >= 50:
            self.fullness -= 10
            self.happiness -= 10
            self.house.eat_fridge += 50
            self.house.money_casket -= 50
            cprint('{} сходила в магазин за едой'.format(self.name), color='yellow')
        else:
            self.happiness -= 10
            cprint('В доме кончились деньги!'.format(self.name), color='yellow')

    def buy_fur_coat(self):
        if self.house.money_casket >= 400:
            self.fullness -= 10
            self.happiness += 60
            self.house.money_casket -= 350
            cprint('{} купила шубу!'.format(self.name), color='yellow')
        else:
            self.happiness -= 10
            cprint('На шубу не хватает денег! Жаль...', color='yellow')

    def clean_house(self):
        if self.house.dirt_house >= 100:
            self.fullness -= 10
            self.happiness -= 10
            self.house.dirt_house -= 100
            cprint('{} убрала в доме! В доме стало чище, грязи: {}!'.format(
                self.name, self.house.dirt), color='yellow')
        else:
            # TODO у нас не полная уборка можно и -5 сделать
            self.fullness -= 10
            self.house.dirt = 0
            cprint('{} убрала! В доме чисто!'.format(self.name), color='yellow')


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)

die_family_member = False
for day in range(366):
    cprint('================== День {} =================='.format(day), color='grey')
    home.dirt_generation()
    serge.who_in_the_shit()
    masha.who_in_the_shit()
    serge.act()
    masha.act()
    cprint('--------------- В конце дня ---------------', color='grey')
    cprint(serge, color='green')
    cprint(masha, color='yellow')
    cprint(home, color='magenta')
    if any([serge.die(), masha.die()]):
        break

# TODO делаем вторую часть

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

"""
home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
"""

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
