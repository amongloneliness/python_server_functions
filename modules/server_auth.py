from sys import argv, exit
from modules.is_auth import *


# Вход в учетную запись.
def server_auth():
    # Проверка наличия входа в учетную запись.
    if is_auth():
        print('Вы уже вошли в учетную запись.')
    else:
        # Проверка операндов.
        if len(argv) < 4:
            print(
                f'{argv[0]} {argv[1]}: пропущены операнды, задающие логин и пароль\n'
                f'По команде «{argv[0]} {SERVER_HELP}» можно получить дополнительную информацию.'
            )
        elif len(argv) > 4:
            print(
                f'{argv[0]} {argv[1]}: получены лишние операнды, задающие логин и пароль\n'
                f'По команде «{argv[0]} {SERVER_HELP}» можно получить дополнительную информацию.'
            )
        else:
            # Открытие файла.
            file_pass = open(FILE_PASS, 'r')

            login = password = ''

            is_login = is_password = False

            for line in file_pass:
                if line[:len(line) - 1] == argv[2] and not is_login:
                    is_login = True
                    login = line[:len(line) - 1]
                elif line[:len(line) - 1] == argv[3] and not is_password:
                    is_password = True
                    password = line[:len(line) - 1]

            if is_login and is_password:
                account = open(FILE_AUTH, "w+")
                account.write(f'{login}\n')
                account.write(f'{password}\n')
                account.close()
            else:
                print('Неверный логин или пароль.')

            # Закрытие файла.
            file_pass.close()

            # Закрытие программы.
            exit()
