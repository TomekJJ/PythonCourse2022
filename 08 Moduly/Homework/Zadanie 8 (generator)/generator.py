# Utwórz generator instancji testowych, który wygeneruje losowe ciągi znaków składające się z jedynie z cyfr od 0-9. Upewnij się, że conajmniej 2 takie same znaki znajdą się w sekwencji.
#
# Zmodyfikuj generator tak, by oczekiwał znaków podanych przez użytkownika np. użytkownik podaje 4 znaki: ‘a’, ‘b’, ‘c’, ‘*’.
#
# Zaimportuj generator bezpośrednio do programu.



import random

# seq = [0,1,2,4,5,6,7,8,9]
n = 8

def get_signs():
    sings = input("podaj znaki do hasła: ")
    seq = list(sings)

    return seq


def generate_pass(seq, n):
    passw = []
    for i in range(n):
        a = random.choice(seq)
        passw.append(a)

    return passw


def check_passw(passw, seq):
    powt = 1
    for i in seq:
        curr_powt = passw.count(i)
        if curr_powt > powt:
            powt = curr_powt
    return powt


def main():
    seq = get_signs()

    while True: # wykonuje się w nieskończoność do czasu spełnienia danego warunku (trzeba dać jakiś warunek stopu czyli "break")
        passw = generate_pass(seq, n)
        powt = check_passw(passw, seq)
        if powt > 2:
            break   # break przerywa działanie pętli jeśli True - wyjdzie z pętli i pójdzie dalej w kodzie

    print("Losowe hasło to; ",  *passw)

main()