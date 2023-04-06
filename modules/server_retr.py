from sys import argv, exit
from os import getcwd
from os.path import exists, isdir
import shutil
from modules.defines import *


# Передача файлов указаных в строке
def server_retr():
    # Проверка операндов.
    if len(argv) < 3:
        print(f'{argv[0]} {argv[1]}: пропущен операнд, задающий файл')
        print(f'По команде «{argv[0]} {SERVER_HELP}» можно получить дополнительную информацию.')
    else:
        for file in argv[2:]:
            # Проверка существования файла / каталога.
            if not exists(file):
                print(f'{argv[0]} {argv[1]}: невозможно отправить файл '
                      f'\'{file}\': Нет такого файла или каталога')

            # Проверка формата файла.
            elif isdir(file):
                print(f'{argv[0]} {argv[1]}: \'{file}\': Это каталог')

            # Копирование файла в директорию программы.
            else:
                shutil.copy2(file, getcwd())

    # Закрытие программы.
    exit()
