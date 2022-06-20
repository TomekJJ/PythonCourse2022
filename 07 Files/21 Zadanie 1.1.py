# Utwórz plik na pulpicie zawierający listę ok. 20 cytatów.
# Każdy cytat powinen się znaleźć w nowej linii.
# Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:
import random

def get_quote(filename):
    with open(f'{filename}.txt') as fopen:
        content = fopen.readlines()

    quote = random.choice(content)
    return quote


def show_quote(quote):
    quote = quote.strip('\n')
    quote = quote.split('-') # tcyta do myślinka

    lenght = len(quote[0]) + 20

    print("\nCytat na dziś to:\n")
    print('*' * lenght)
    print(quote[0].center(lenght))
    print(f'~ {quote[1]} ~'.center(lenght))
    print('*' * lenght)


def main():
    filename = input("podaj nazwę pliku: ")
    quote = get_quote(filename)
    show_quote(quote)


main()