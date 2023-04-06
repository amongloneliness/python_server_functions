from os import listdir
from os.path import isfile
from sys import exit


# Список файлов каталога программы.
def server_list():
    for element in listdir():
        if isfile(element):
            print(element)

    # Завершение программы.
    exit()
