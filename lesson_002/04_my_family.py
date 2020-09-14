#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mom', 'dad', 'brother', 'grandmother', 'grendfather']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['Ирина', 165],
    ['Сергей', 179],
    ['Олег', 175],
    ['Людмила', 160],
    ['Николай', 170],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца - ' + str(my_family_height[1][1]) + ' см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

stature = int(my_family_height[0][1]) + int(my_family_height[1][1]) \
+ int(my_family_height[2][1]) + int(my_family_height[3][1]) + int(my_family_height[4][1])
print('Общий рост моей семьи ' + str(stature) + ' см')