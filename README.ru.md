***
### Описание
Репозиторий содержит программу, выполняющую функции сервера, способную выполнять команды:
1. auth user pass — авторизация, user и pass хранятся в файле pass в каталоге запуска
программы
2. list — показать список файлов в каталоге запуска программы
3. info file — напечатать сведения о файле, mime тип, размер, время создания
4. retr file1 file2 file_n — передать файлы, указанные в строке.
5. exit — выход
6. help — справка по командам.

Файл **pass** содержит 2 строки: логин и пароль пользователя для входа. [его наличие обязательно]

---

Чтобы скомпилировать программу при наличии python3 необходимо установить модуль pyinstaller.
> **pip3 install pyinstaller**

Компиляция программы выполняется в папке репозитория:
> **sh scripts/make.sh**

Также, удаление лишних файлов, после сборки, проекта:
> **sh scripts/clean.sh**

Полное удаление файлов после сборки:
> **sh scripts/fclean.sh**
