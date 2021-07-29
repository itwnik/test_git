# -*- coding: utf-8 -*-

# import os
# import time
# import shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


import os
import time
import shutil


INPUT_PATH = 'icons'
OUTPUT_PATH = 'icons_by_year'


class FileYears:

    def __init__(self, input_path, out_path):
        self.input_path = input_path
        self.out_path = out_path
        self.input_path_sort = ''
        self.out_path_sort = ''
        self.full_file_path_out = ''

    def normalize_path(self):
        self.input_path_sort = os.path.normpath(os.path.join(os.path.dirname(__file__), self.input_path))
        self.out_path_sort = os.path.normpath(os.path.join(os.path.dirname(__file__), self.out_path))

    def create_dir(self, file_mod_time):
        self.full_file_path_out = os.path.join(self.out_path_sort, str(file_mod_time.tm_year),
                                               str(file_mod_time.tm_mon))
        if not os.path.exists(self.full_file_path_out):
            os.makedirs(self.full_file_path_out)

    def copy_file(self, full_file_path, file):
        shutil.copy2(full_file_path, self.full_file_path_out)
        print(f"Copy file '{file}' completed!")

    def parsing_dir(self):
        for self.dir_path, self.dir_names, self.file_names in os.walk(self.input_path_sort):
            for file in self.file_names:
                full_file_path = os.path.join(self.dir_path, file)
                file_mod_time = time.gmtime(os.path.getmtime(full_file_path))
                self.create_dir(file_mod_time)
                self.copy_file(full_file_path, file)

    def starting(self):
        self.normalize_path()
        self.parsing_dir()


copy_file = FileYears(INPUT_PATH, OUTPUT_PATH)
copy_file.starting()

# TODO предлагаю вам сделать вторую часть

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
