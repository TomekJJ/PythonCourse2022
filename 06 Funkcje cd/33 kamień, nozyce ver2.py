import random

WINNERS = {
    'k': 'n',  # wygrany : pokonany
    'n': 'p',
    'p': 'k'
}

CORRECT_VALUES = ('k', 'p', 'n')

def get_user():
    while True:
        user = input("kamień(k), nożyce(n), papier(p) ? -->")
        if user in CORRECT_VALUES:
            break

    return user


def get_comp():
    values = ['k', 'p', 'n']
    comp = random.choice(CORRECT_VALUES)
    print(f'Komputer pokazał {comp}')


def show_result(comp, user):
    pass
    if user == comp:
        print('Remis!')
    elif WINNERS[user] == comp:  # podstawiamy wartość użytkownia pod klucz słownika "winners"
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