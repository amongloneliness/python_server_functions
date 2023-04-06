***
### Description
The repository contains a program that acts as a server, capable of executing commands:
1. auth user pass - authorization, user and pass are stored in the pass file in the launch directory
programs
2. list - show a list of files in the program launch directory
3. info file - print information about the file, mime type, size, creation time
4. retr file1 file2 file_n - transfer the files specified in the line.
5. exit - exit
6. help - help on commands.

The **pass** file contains 2 lines: username and password for login. [its presence is required]

---

To compile the program with python3, you need to install the pyinstaller module.
> **pip3 install pyinstaller**

The program is compiled in the repository folder:
> **sh scripts/make.sh**

Also, deleting unnecessary files, after assembly, of the project:
> **sh scripts/clean.sh**

Complete removal of files after build:
> **sh scripts/fclean.sh**
