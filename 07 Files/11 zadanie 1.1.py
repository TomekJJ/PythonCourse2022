# Utwórz plik na pulpicie zawierający listę ok. 20 cytatów.
# Każdy cytat powinen się znaleźć w nowej linii.
# Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:
import random

def get_quote():
    with open('cytaty.txt', encoding='utf-8') as fopen:
        content = fopen.readlines()

    quote = random.choice(content)
    return quote


def show_quote(quote):
    quote = get_quote()
    quote = quote.strip('\n')

    lenght = len(quote) + 20

    print("\nCytat na dziś to:\n")
    print('*' * lenght)
    print(quote.center(lenght))
    print('*' * lenght)


def main():
    quote = get_quote()
    show_quote(quote)


main()