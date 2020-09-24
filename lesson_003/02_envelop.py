# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта,
# если размеры равны - лист входит в конверт впритирку)
# Не забывайте, что лист бумаги можно перевернуть и попробовать вставить в конверт другой стороной.
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные


def test_convert(height_convert, width_convert, height_paper, width_paper):
    if height_convert >= height_paper and width_convert >= width_paper:
        print(f"В конверт размером {height_convert} x {width_convert} "
              f"входит лист бумаги {height_paper} x {width_paper}")
    elif height_convert >= width_paper and width_convert >= height_paper:
        print(f"В конверт размером {height_convert} x {width_convert} "
              f"входит лист бумаги {height_paper} x {width_paper} если перевернуть")
    else:
        print(f"В конверт размером {height_convert} x {width_convert} "
              f"НЕ входит лист бумаги {height_paper} x {width_paper}")
# TODO может ли функция ничего не возвращать?
# TODO надеюсь не против что я поэксперементировал с задачами?


envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
test_convert(envelop_x, envelop_y, paper_x, paper_y)
# проверить для
paper_x, paper_y = 9, 8
test_convert(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 6, 8
test_convert(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 8, 6
test_convert(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 3, 4
test_convert(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 11, 9
test_convert(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 9, 11
test_convert(envelop_x, envelop_y, paper_x, paper_y)

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

# hole_x, hole_y = 8, 9
# brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)




def test_hole(hole_height, hole_width, brick_height, brick_width, brick_lenght):
    if hole_height >= brick_height and hole_width >= brick_width:
        print(
            f"кирпич размером {brick_height}x{brick_width}x{brick_lenght} "
            f"войдет в прямоугольное отверстие размером {hole_height}x{hole_width}")
    elif hole_height >= brick_width and hole_width >= brick_height:
        print(
            f"кирпич размером {brick_height}x{brick_width}x{brick_lenght} "
            f"войдет в прямоугольное отверстие размером {hole_height}x{hole_width} если покрутить")
    elif hole_height >= brick_lenght and hole_width >= brick_width:
        print(
            f"кирпич размером {brick_height}x{brick_width}x{brick_lenght} "
            f"войдет в прямоугольное отверстие размером {hole_height}x{hole_width} если покрутить")
    elif hole_width >= brick_height and hole_width >= brick_lenght:
        print(
            f"кирпич размером {brick_height}x{brick_width}x{brick_lenght} "
            f"войдет в прямоугольное отверстие размером {hole_height}x{hole_width} если покрутить")
    elif hole_width >= brick_lenght and hole_width >= brick_height:
        print(
            f"кирпич размером {brick_height}x{brick_width}x{brick_lenght} "
            f"войдет в прямоугольное отверстие размером {hole_height}x{hole_width} если покрутить")
    else:
        print(
            f"кирпич размером {brick_height}x{brick_width}x{brick_lenght} "
            f"НЕ войдет в прямоугольное отверстие размером {hole_height}x{hole_width}")


hole_x, hole_y = 8, 9
brick_x, brick_y, brick_z = 11, 10, 2
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 11, 2, 10
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 10, 11, 2
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 10, 2, 11
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 2, 10, 11
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 2, 11, 10
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 5, 6
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 6, 5
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 3, 5
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 5, 3
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 5, 6, 3
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 5, 3, 6
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 11, 3, 6
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 11, 6, 3
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 11, 3
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 3, 11
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 6, 11
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 11, 6
test_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
