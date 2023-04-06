from sys import exit
from os import remove
from os.path import exists
from modules.defines import *


# Завершение работы.
def server_exit():
    # Проверка наличия файла аутефикации.
    if exists(FILE_AUTH):
        remove(FILE_AUTH)
    else:
        print('Вы не вошли в аккаунт')

    # Завершение работы программы.
    exit()

