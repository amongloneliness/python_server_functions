from sys import argv, exit
from modules.defines import *


# Вывод запрета вызова команды без входа в аккаунт.
def server_auth_fail():
    print(
        f'Чтобы воспользоваться «{argv[1]}», войдите в аккаунт\n'
        f'По команде «{argv[0]} {SERVER_HELP}» можно получить дополнительную информацию.'
    )

    # Завершение программы.
    exit()