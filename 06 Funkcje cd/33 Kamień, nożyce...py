import random

def game(user, komp):
    if komp == 'k':
        if user == 'n':
            print("przegrałeś")
        elif user == 'p':
            print('wygrałeś')
        else:
            print("remis")

    if komp == 'n':
        if user == 'p':
            print("przegrałeś")
        elif user == 'k':
            print('wygrałeś')
        else:
            print("remis")

    if komp == 'p':
        if user == 'k':
            print("przegrałeś")
        elif user == 'n':
            print('wygrałeś')
        else:
            print("remis")

def next_game():
    while input('Would you like to continue (Y/N) -> ') == 'Y':
        # user
        user = input("kamień(k), nożyce(n), papier(p) ? -->")

        # komputer
        seq = ['k', 'n', 'p']
        komp = random.choice(seq)
        print(f'Komputer pokazał {komp}')

        game(user, komp)

    else:
        print('koniec')


game(user, komp)
next_game(user, komp)