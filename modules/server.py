from modules.server_auth import server_auth
from modules.server_list import server_list
from modules.server_info import server_info
from modules.server_retr import server_retr
from modules.server_exit import server_exit
from modules.server_help import server_help
from modules.server_fail import server_fail
from modules.server_auth_fail import server_auth_fail
from modules.is_auth import is_auth
from sys import argv, exit
from modules.defines import *


def server():
    # Проверка количества атрибутов.
    if len(argv) == 1:
        server_fail()

    # Результат проверки активации аккаунта.
    active_account = is_auth()

    # Справка по командам.
    if argv[1] == SERVER_HELP:
        server_help()

    # Вход в учетную запись
    elif argv[1] == SERVER_AUTH:
        server_auth()

    # Выход из учетной записи
    elif argv[1] == SERVER_EXIT:
        server_exit()

    # Вывод списка файлов в каталоге.
    elif argv[1] == SERVER_LIST:
        # Проверка аккаунта.
        if active_account:
            server_list()
        else:
            server_auth_fail()

    # Вывод информации о файле.
    elif argv[1] == SERVER_INFO:
        # Проверка аккаунта.
        if active_account:
            server_info()
        else:
            server_auth_fail()

    # Перенос файлов в рабочий каталог.
    elif argv[1] == SERVER_RETR:
        # Проверка аккаунта.
        if active_account:
            server_retr()
        else:
            server_auth_fail()
    else:
        print(f'{argv[0]}: неверный атрибут «{argv[1]}»')
        print(f'По команде «{argv[0]} {SERVER_HELP}» можно получить дополнительную информацию.')

    # Завершение программы.
    exit()
