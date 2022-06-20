# 3▹ Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
# Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
# Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.

import os


def open_file(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            print(f.read())

    else:
        print('Nie ma takiego pliku')


def save_file(filename):
    pass


def main():
    filename = input("podaj nazwę pliku", )
    #filename = [filename + "txt"]
    read_file(filename)


main()