import random

ZBIOR_HASEL = ["tommek", "mmichal", "ania"]


def losuj_haslo():
    pswrd = random.choice(ZBIOR_HASEL)
    print("Wylosowane hasło to:", pswrd)  # do usunięcia
    return pswrd

def print_emtpy_pass(pswrd):
    pswrd_len = len(pswrd)
    empty_pswrd = pswrd_len * '_'
    print(f'**** Hasło składa się z {pswrd_len} liter ****')
    print(list(empty_pswrd))
    return list(empty_pswrd)

def find_letter(pswrd, ingame_pswrd):
    pswrd = list(pswrd)
    letter = input("Zgadnij literę -->")

    if letter in pswrd:
        for i, v in enumerate(pswrd):  # i to indeks, v to wartość
            if letter == v:
                ingame_pswrd[i] = letter
        print(ingame_pswrd)
        return ingame_pswrd
    else:
        print("W haśle nie ma takiej litery")
        print(ingame_pswrd)
        return ingame_pswrd

def main():

    pswrd = losuj_haslo()

    ingame_pswrd = print_emtpy_pass(pswrd)

    for proba in range (1, 7):
        print(f'***** Próba {proba} *****')
        if ingame_pswrd == list(pswrd):
            print("Brawo wygrałeś")
            break
        else:
            find_letter(pswrd, ingame_pswrd)

        if proba == 6:
            print("Przegrałeś, spróbuj jeszcze raz")
            break
main()
