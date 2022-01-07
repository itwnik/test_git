# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

import argparse
from PIL import Image, ImageDraw, ImageFont, ImageColor

TICKET_PATH = "images/ticket_template.png"
TICKET_SAVE_PATH = "images/ticket_full.png"


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fio', nargs='+', required=True, help='обязательный, фамилия имя отчество.')
    parser.add_argument('--from_', type=str, required=True, help='обязательный, откуда летим.')
    parser.add_argument('--to', type=str, required=True, help='обязательный, куда летим.')
    parser.add_argument('--date', type=str, required=True, help='обязательный, когда летим.')
    parser.add_argument('--save_to', default=TICKET_SAVE_PATH,
                        help='необязательный, путь для сохранения заполненнего билета.')
    return parser


def make_ticket(fio, from_, to, date, save_to):
    ticket = Image.open(TICKET_PATH)
    full_ticket_draw = ImageDraw.Draw(ticket)

    text_fio_ticket = fio
    text_from_ticket = from_
    text_to_ticket = to
    text_date_ticket = date
    font_ticket = ImageFont.truetype("python_snippets/fonts/ofont.ru_Source_Seri_fPro.ttf", size=14)

    full_ticket_draw.text((45, 122), text_fio_ticket, font=font_ticket, fill=ImageColor.colormap["black"])
    full_ticket_draw.text((45, 190), text_from_ticket, font=font_ticket, fill=ImageColor.colormap["black"])
    full_ticket_draw.text((45, 256), text_to_ticket, font=font_ticket, fill=ImageColor.colormap["black"])
    full_ticket_draw.text((285, 256), text_date_ticket, font=font_ticket, fill=ImageColor.colormap["black"])

    ticket.save(save_to)


if __name__ == '__main__':
    try:
        parser = create_parser()
        ticket_info = parser.parse_args()
        make_ticket(' '.join(text for text in ticket_info.fio),
                    ticket_info.from_, ticket_info.to, ticket_info.date, ticket_info.save_to)
    except SystemExit as exp:
        print("Нет обязательных параметров!")

# TODO скрипты для запуска:
#   python 01_ticket.py - -fio Иванов И.И. --from Ростов --to Москва - -date 01.01.2022
#   python 01_ticket.py - -fio Иванов И.И. --from Ростов --to Москва - -date 01.01.2022 --save_to images/test.png

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
# Зачет!
