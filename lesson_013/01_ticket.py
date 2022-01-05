# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


from PIL import Image, ImageDraw, ImageFont, ImageColor

TICKET_PATH = "images/ticket_template.png"


def make_ticket(fio, from_, to, date):
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

    ticket.save("images/full_ticket.png")


if __name__ == '__main__':
    make_ticket('Petrov A.A.', 'Rostov-on-Don', 'Moscow', '01.01.22')


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