## do dokończenia zadanie

# Rozpoznawanie kart.
# Utwórz plik zawierający numery kart kredytowych.
# Sprawdź dla każdej kart jej typ.
# Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt.

def read():
    with open('card_numbers') as fopen:
        content = fopen.readlines()
    return content

def save():
    with open(f'{type}.txt', 'w')


def is_card(number):
    # Z operatorem trójargumentowym
    return number.isdigit() and 13 <= len(number) <= 16  # zwraca tylko true or false
    #inaczej można z ifami


def is_visa(number):
   return len(number) in [13, 16] and number[0] == '4'  # if len(number) == 16 or len(number) == 13:
    # można też pełne pętle
    #        return True
    # else:
    #    return False


def is_mastercard(number):
    if len(number) == 16 and (51 <= int(number[0:2]) <= 55 or int(number[0:4]) in range(2221, 2720 +1)):     # UWaga wycinami/dodajemy + 1 bo ostatnia pozycja już nie wchodzi
        return True
    else:
        return False


def is_ae(number):
    if len(number) == 15 and number.startswith(('34','37')):
        return True
    else:
        return False

def main():
    card_list = read()

    for number in card_list:
        if is_visa(number):
            print('To jest Visa')
        elif is_mastercard(number):
            print('To jest Matestercard')
        elif is_ae(number):
            print('To jest American Express')
        else:
            print('Nieznany typ karty')


main()