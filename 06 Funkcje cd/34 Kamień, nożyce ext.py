import random

WINNERS = {
    'k': ('n', 'j'),  # wygrany : pokonany
    'n': ('p', 'j'),
    'p': ('k', 's'),
    'j': ('p', 's'),
    's': ('n', 'k')
}

CORRECT_VALUES = ('k', 'p', 'n', 'j', 's')

def get_user():
    while True:
        user = input("kamień(k), nożyce(n), papier(p), spock(s), jaszczurka(j)? -->")
        if user in CORRECT_VALUES:
            break

    return user


def get_comp():
    comp = random.choice(CORRECT_VALUES)
    return comp

def show_result(comp, user):
    pass
    if user == comp:
        print('Remis!')
    elif comp == WINNERS[user]:  # podstawiamy wartość użytkownia pod klucz słownika "winners"
        print('Wygrałeś!')
    else:
        print('Przegrałeś!')


def main():
    while True:
        print('**** Gra Kamień - Nożyce - Papier ****')
        user = get_user()
        comp = get_comp()

        show_result(comp, user)

        play_again = input('Czy zagrać ponowanie [T / N]? ')

        if play_again == "N":
            break

    print('Dzięki za grę!')

main()
