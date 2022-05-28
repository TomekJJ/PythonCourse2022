import random

ZBIOR_HASEL = ["tommek", "mmichał", "ania"]


def losuj_haslo():
    pswrd = random.choice(ZBIOR_HASEL)
    print("Wylosowane hasło to:", pswrd)  # do usunięcia
    return pswrd

def print_emtpy_pass(pswrd):
    pswrd_len = len(pswrd)
    empty_pswrd = pswrd_len * ' _ '
    print(f'**** Hasło składa się z {pswrd_len} liter ****')
    print(empty_pswrd)
    return empty_pswrd

def find_letter(pswrd, ingame_pswrd):

    pswrd = tuple(pswrd)
    letter = input("Zgadnij literę -->")

    if letter in pswrd:
        for i, v in enumerate(pswrd):  # i to indeks, v to wartość
            if letter == v:
                ingame_pswrd[i] = letter
        print(ingame_pswrd)
        return ingame_pswrd
    else:
        print("W haśle nie ma takiej litery")

#def main():
empty_pswrd = []
pswrd = losuj_haslo()

print_emtpy_pass(pswrd)

ingame_pswrd = empty_pswrd

for proba in range (1, 5):
    print(f'***** Próba {proba} *****')
    find_letter(pswrd, ingame_pswrd)

#main()
