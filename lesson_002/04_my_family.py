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
# стараемся конкатенацию строк в принте не использовать, либо через (,)
# самый новый формат для печати в принт это f - строки или более ранний .format()
# преобразование к str делать не нужно принт и так распечатает!
# Поправил
print(f"Рост отца - {my_family_height[1][1]} см")

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
# преобразование к инт тут делать не нужно тем более каждого элемента! Не используем знак \ для переноса, возьмите
# в скобки и перенесите по математическому знаку!
# готово
stature = (my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] +
           my_family_height[3][1] + my_family_height[4][1])
# аналогично

print(f"Общий рост моей семьи {stature} см")

# зачет!
