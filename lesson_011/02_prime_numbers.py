# -*- coding: utf-8 -*-

# Есть функция генерации списка простых чисел

def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


# class PrimeNumbers:
#     def __init__(self, n):
#         self.n = n
#         self.prime_numbers = []
#         self.new_start = 2
#
#     def __iter__(self):
#         self.iter_number = -1
#         return self
#
#     def __next__(self):
#         self.iter_number += 1
#         for self.number in range(self.new_start, self.n + 1):
#             for prime in self.prime_numbers:
#                 if self.number % prime == 0:
#                     break
#             else:
#                 self.prime_numbers.append(self.number)
#                 self.new_start = self.number
#                 return self.number
#         raise StopIteration()
#
#
# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)

# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


# for number in prime_numbers_generator(n=10000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True

# ##Part_3.1##
def filter_lucky_number(in_number):
    numbers = list(map(int, str(in_number)))
    formula = int((len(numbers) - 1) / 2)
    if len(numbers) >= 3:
        if sum(numbers[:formula]) == sum(numbers[-formula:]):
            return True
        else:
            return False
    return False

# для проверки раскомментить
# for number in prime_numbers_generator(n=10000):
#     print(number, filter_lucky_number(number))
# ##################

# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101

# ##Part_3.2##
def filter_lucky_number_two(in_number):
    numbers = list(map(int, str(in_number)))
    if len(numbers) >= 2 and numbers == list(reversed(numbers)):
        return True
    else:
        return False

# для проверки раскомментить
# for number in prime_numbers_generator(n=10000):
#     print(number, filter_lucky_number_two(number))
# ##################

# 3) придумать свою (https://clck.ru/GB5Fc в помощь)


# ##Part_3.3##
def filter_lucky_number_three(in_number):  # Триморфное число https://clck.ru/SoJih
    if str(in_number) == str(in_number**3)[-len(str(in_number)):]:
        return True
    else:
        return False

# для проверки раскомментить
# for number in prime_numbers_generator(n=10000):
#     print(number, filter_lucky_number_three(number))
# ##################

# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.


# ##Part_3.3.1## method_1
def prime_numbers_generator_two(n, func):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            # функцию нужно принять на вход функции а не брать из вне
            #  а в чем разница? типабольше расширености кода и можно передать разные функции?

            # если мы перенесем функцию то все сломается и так да для расширения кода
            # TODO функцию назвать как filter_func чтобы было понятно
            if func(number):
                yield number


#  для проверки раскомментить
for number_2 in prime_numbers_generator_two(n=10000, func=filter_lucky_number_three):
    print(number_2, filter_lucky_number_three(number_2))
# ##################


# ##Part_3.3.2## method_2
def prime_numbers_generator_three(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number

#  для проверки раскомментить
# for number_2 in prime_numbers_generator_three(n=10000):
#     if filter_lucky_number(number_2):
#         print(number_2)
# ##################


