# Wróć do pierwszego zadania z lekcji o plikach, zmodyfikuj go tak, aby to użytkownik podawał nazwę pliku z cytatami.
# Pamiętaj, by użytkownik po wykonaniu błędnej akcji (np. literówki w nazwie pliku) miał możliwość poprawić swój błąd.

import random
import os


def get_quote(filename):
    with open(filename, encoding = "UTF-8") as fopen:
        content = fopen.readlines()

    quote = random.choice(content)
    return quote


def show_quote(quote):
    quote = quote.strip('\n')
    quote = quote.split('-') # cytat do myślinka

    lenght = len(quote[0]) + 20

    print("\nCytat na dziś to:\n")
    print('*' * lenght)
    print(quote[0].center(lenght))
    print(f'~ {quote[1]} ~'.center(lenght))
    print('*' * lenght)


def open_file():
    while True:
        try:
            filename = input("podaj nazwę pliku (bez rozszerzenia): ") + ".txt"
            if not os.path.exists(filename):
                raise FileNotFoundError
        except Exception:
            print("Nie ma takiego pliku. Spróbuj jeszcze raz")
        else:
            return filename


def main():
    filename = open_file()
    quote = get_quote(filename)
    show_quote(quote)


main()