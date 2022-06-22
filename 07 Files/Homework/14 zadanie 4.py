# Wyświetl 3 losowe cytaty
import random

def get_quote():
    with open('cytaty.txt', encoding='utf-8') as fopen:
        content = fopen.readlines()

    quote = random.choice(content)
    return quote


def show_quote(quote):
    quote = quote.strip('\n')
    quote = quote.split('-') # cytat do myślinka

    lenght = len(quote[0]) + 20

    print('*' * lenght)
    print(quote[0].center(lenght))
    print(f'~ {quote[1]} ~'.center(lenght))
    print('*' * lenght)


def main():
    quote1 = get_quote()
    print("\nPierwszy cytat na dziś to:\n")
    show_quote(quote1)

    quote2 = get_quote()
    print("\nDrugi cytat na dziś to:\n")
    show_quote(quote2)

    quote3 = get_quote()
    print("\nTrzeci cytat na dziś to:\n")
    show_quote(quote3)

main()