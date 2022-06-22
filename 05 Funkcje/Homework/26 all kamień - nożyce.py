# Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.

import random

WINNERS = {
    'k': 'n',
    'n': 'p',
    'p': 'k'
}


def get_comp():
    values = ('k', 'n', 'p')
    comp = random.choice(values)

    return comp


def get_user():
    values = ('k', 'n', 'p')
    while True:
        user = input("kamień(k), nożyce(n), papier(p) ? -->")
        if user in values:
            break

    return user


def show_result(comp, user):
    if user == comp:
        print('Remis!')
    elif WINNERS[user] == comp:  # podstawiamy wartość użytkownia pod klucz słownika "winners"
        print('Wygrałeś!')
    else:
        print('Przegrałeś!')


def main():
    comp = get_comp()
    user = get_user()
    print(f'Komputer pokazał {comp}')


    show_result(comp, user)


main()


