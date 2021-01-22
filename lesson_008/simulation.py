# -*- coding: utf-8 -*-
"""

Симуляция.

Его нужно делать в отдельном файле, скопировав тут нужные классы из 01 и написать новый класс симуляции.
В классах семьи убрать все принты из кода и метод стр они нам не нужны, нам нужна только логика их работы!
В классе симуляция у вас будут следующие методы, во первых инит, метод_обнуления всех объектов(создание заново),
метод_добавления котов (по количеству), метод запуска цикла на один год который будет возвращать TRUE если дойдет
до конца, методы которые генерят инциденты с едой и деньгами(вот и хаус), и сам метод эксперимент в котором мы будем
запускать нашу симуляцию три раза!

"""
from random import randint, choice
from typing import List


class House:

    def __init__(self):
        self.money_casket = 100
        self.eat_fridge = 50
        self.dirt_house = 0
        self.food_cat = 30

    def dirt_generation(self):
        self.dirt_house += 5


class Human:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house

    def eat(self, eat_count=20):

        if self.house.eat_fridge >= eat_count:
            self.fullness += eat_count
            self.house.eat_fridge -= eat_count
        else:
            self.fullness -= 10

    def who_in_the_shit(self):
        if self.house.dirt_house >= 90:
            self.happiness -= 10

    # --------------cat_act----------------------
    def pat_the_cat(self):
        self.happiness += 5

    def buy_food_cat(self):
        if self.house.money_casket >= 50:
            self.house.money_casket -= 40
            self.house.food_cat += 40
            self.fullness -= 10
        else:
            self.fullness -= 10

    # --------------end_cat_act----------------------

    def die(self):
        if self.fullness == 0 or self.happiness < 10:
            return True


class Husband(Human):

    def __init__(self, name, house, salary_man):
        super().__init__(name=name, house=house)
        self.salary_man = salary_man

    def act(self):
        magic_ball = randint(1, 8)
        if self.fullness <= 20:
            self.eat()
        elif self.house.money_casket < 350:
            self.work()
        elif magic_ball == 3:
            self.eat()
        elif magic_ball == 4:
            self.pat_the_cat()
        elif magic_ball == 6:
            self.work()
        else:
            self.gaming()

    def work(self):
        self.fullness -= 10
        self.happiness -= 10
        self.house.money_casket += self.salary_man

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20


class Wife(Human):

    def act(self):
        magic_ball = randint(1, 9)
        if self.fullness <= 20:
            self.eat()
        elif self.house.eat_fridge <= 50:
            self.shopping()
        elif self.house.food_cat <= 30:
            self.buy_food_cat()
        elif magic_ball == 1:
            self.pat_the_cat()
        elif magic_ball == 2:
            self.eat()
        elif magic_ball == 4:
            self.buy_fur_coat()
        elif magic_ball == 6:
            self.shopping()
        elif magic_ball == 7:
            self.clean_house()
        else:
            self.clean_house()

    def shopping(self):
        if self.house.money_casket >= 70:
            self.fullness -= 10
            self.happiness -= 10
            self.house.eat_fridge += 70
            self.house.money_casket -= 70
        else:
            self.happiness -= 10

    def buy_fur_coat(self):
        if self.house.money_casket >= 400:
            self.fullness -= 10
            self.happiness += 60
            self.house.money_casket -= 350
        else:
            self.happiness -= 10

    def clean_house(self):
        if self.house.dirt_house >= 100:
            self.fullness -= 10
            self.happiness -= 10
        elif self.house.dirt_house >= 5:
            self.happiness += 5
            self.fullness -= 5
            self.house.dirt_house = 0


class Child(Human):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def act(self):
        if self.fullness < 20:
            self.eat(eat_count=10)
        else:
            self.sleep()

    def eat(self, **kwargs):
        super().eat(**kwargs)

    def sleep(self):
        self.fullness -= 10


class Cat:

    def __init__(self, name_cat, house):
        self.name = name_cat
        self.fullness_cat = 30
        self.house = house

    def act(self):
        magic_ball = randint(6, 12)
        if self.fullness_cat <= 30:
            self.eat_cat()
        elif magic_ball == 7:
            self.cat_dirt_generation()
        elif magic_ball == 9:
            self.eat_cat()
        elif magic_ball == 11:
            self.cat_dirt_generation()
        else:
            self.sleep()

    def eat_cat(self):
        if self.house.food_cat >= 10:
            self.fullness_cat += 20
            self.house.food_cat -= 10
        else:
            self.fullness_cat -= 10

    def sleep(self):
        self.fullness_cat -= 10

    def cat_dirt_generation(self):
        self.fullness_cat -= 10
        self.house.dirt_house += 5

    def die(self):
        if self.fullness_cat <= 0:
            return True


class Simulation:
    name_cat: List[str]

    def __init__(self, food_incidents, money_incidents):
        self.food_incidents = food_incidents  # переменные инцедентов
        self.money_incidents = money_incidents  # переменные инцедентов
        self.cats = []  # список котов
        self.citizens = []
        self.fail_money_day = []  # Список дней в которые будут происходить инцеденты
        self.fail_food_day = []  # Список дней в которые будут происходить инцеденты
        self.home = House()
        self.serge = Husband(name='Сергей', house=self.home, salary_man=self.salary)
        self.masha = Wife(name='Маша', house=self.home)
        self.maks = Child(name='Макс', house=self.home)
        self.citizens = [self.serge, self.masha, self.maks]

    def restart_zero(self):
        # TODO вот так мы обнуляемся, очень просто пересоздать класс
        # self.home = House()
        # self.serge = Husband(name='Сергей', house=self.home, salary_man=self.salary)
        # self.masha = Wife(name='Маша', house=self.home)
        # self.maks = Child(name='Макс', house=self.home)
        # self.citizens = [self.serge, self.masha, self.maks]
        self.cats.clear()  # чистим список котов
        self.citizens.clear()
        self.fail_food_day.clear()  # чистим список дней с инцедентами
        self.fail_money_day.clear()  # чистим список дней с инцедентами

    def life(self):
        for day in range(1, 366):
            self.home.dirt_generation()
            self.serge.who_in_the_shit()
            self.masha.who_in_the_shit()
            self.food_fail(day)
            self.money_fail(day)
            for citizen in self.citizens:
                citizen.act()
            if any([citizen.die() for citizen in self.citizens]):
                return False
        return True

    def get_pussy(self, count):
        # TODO список убираем
        self.name_cat = ['Арбузик', 'Агроном', 'Анчоус', 'Апельсин']
        # TODO тут в цикле заводим переменную i и по ней формируем имя кот номер 0 1 2 3
        for _ in range(count):
            auto_cat = Cat(name_cat=choice(self.name_cat), house=self.home)  # TODO мало имен на бы 10 хотябы
            self.cats.append(auto_cat)

    def incidents_generation(self):
        for _ in range(self.money_incidents):
            self.fail_money_day.append(randint(2, 356))
        for _ in range(self.food_incidents):
            self.fail_food_day.append(randint(2, 365))

    def food_fail(self, day):
        if day in self.fail_food_day:
            self.home.eat_fridge = int(self.home.eat_fridge / 2)

    def money_fail(self, day):
        if day in self.fail_money_day:
            self.home.money_casket = int(self.home.money_casket / 2)

    def experiment(self, salary):
        # TODO self.serge.salary = salary
        # я долго с этим голову ломал. не понимаю. мы создали экземпляр класса МУЖ. при создании зарплату ему не передали!
        #   как мы передадим зарплату уже созданному экземпляру?
        for cats in range(10, 0, -1):  # заводим цикл по количеству котов от 10 до 0 с шагом -1
            verification = 1  # объявляем переменную которая будет отвечать за верификацию
            for _ in range(3):  # заводим цикл по range(3)
                self.restart_zero()
                # self.family_create()
                # TODO вот тут мы пишем код которые передает зарплату
                self.__init__()
                self.salary = salary
                self.get_pussy(count=cats)  # создаем нужное количество котов
                self.incidents_generation()  # генерируем дни, в которые будут происходить инцеденты
                self.citizens.extend(self.cats)
                if self.life():
                    verification += 1
                    if verification == 2:
                        return cats
        return 0


for food_incidents in range(6):
    for money_incidents in range(6):
        life = Simulation(money_incidents, food_incidents)
        for salary in range(50, 401, 50):
            max_cats = life.experiment(salary)
            print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

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
