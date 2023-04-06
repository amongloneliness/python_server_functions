from sys import argv, exit


# Обработка отсутствия аргументов.
def server_fail():
    print(f'{argv[0]}: пропущен операнд')
    print(f'По команде «{argv[0]} help» можно получить дополнительную информацию.')

    # Завершение программы.
    exit()
