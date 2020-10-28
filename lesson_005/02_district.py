# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as center_house1_room1
from district.central_street.house1.room2 import folks as center_house1_room2
from district.central_street.house2.room1 import folks as center_house2_room1
from district.central_street.house2.room2 import folks as center_house2_room2
from district.soviet_street.house1.room1 import folks as soviet_house1_room1
from district.soviet_street.house1.room2 import folks as soviet_house1_room2
from district.soviet_street.house2.room1 import folks as soviet_house2_room1
from district.soviet_street.house2.room2 import folks as soviet_house2_room2

district = [*center_house1_room1,
            *center_house1_room2,
            *center_house2_room1,
            *center_house2_room2,
            *soviet_house1_room1,
            *soviet_house1_room2,
            *soviet_house2_room1,
            *soviet_house2_room2,
            ]

print(f"На районе живут {', '.join(district)}")

# зачет!
