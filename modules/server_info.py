from sys import argv, exit
from os.path import exists, isdir, getsize, getctime
import mimetypes as mime
import time
from modules.defines import *


# Информация о файлах.
def server_info():
    # Проверка операндов.
    if len(argv) < 3:
        print(f'{argv[0]} {argv[1]}: пропущен операнд, задающий файл')
        print(f'По команде «{argv[0]} {SERVER_HELP}» можно получить дополнительную информацию.')
    else:
        # Вывод файлов.
        for file in argv[2:]:
            # Вывод (mime типа / размера / даты создания) файла.
            if exists(file) and not isdir(file):
                file_type = mime.guess_type(file)[0]
                file_size = getsize(file)
                file_date = time.ctime(getctime(file))

                print('%20s:   %13s    %10s    %15s' % (file, file_type, file_size, file_date))
        
        # Вывод ошибочных файлов и директорий.
        for file in argv[2:]:
            # Проверка существования файла.
            if not exists(file):
                print(f'{argv[0]} {argv[1]}: невозможно вывести информацию о файле '
                      f'\'{file}\': Нет такого файла или каталога')

            # Проверка формата файла.
            elif isdir(file):
                print(f'{argv[0]} {argv[1]}: \'{file}\': Это каталог')

    # Завершение программы.
    exit()
