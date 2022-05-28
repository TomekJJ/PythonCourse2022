# Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
    # Co wiemy o tych numerach tych kart?
    # All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
    # MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
    # American Express card numbers start with 34 or 37 and have 15 digits.

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
    while True: # wykonuje się w nieskończoność do czasu spełnienia danego warunku (trzeba dać jakiś warunek stopu czyli "break")
        card_number = input('podaj numer karty do sprawdzenia ->').replace(' ','')
        if is_card(card_number):
            break   # break przerywa działanie pętli jeśli True - wyjdzie z pętli i pójdzie dalej w kodzie
        else:
            print("To nie jest prawidłowy numer karty")

    if is_visa(card_number):
        print('To jest Visa')
    elif is_mastercard(card_number):
        print('To jest Matestercard')
    elif is_ae(card_number):
        print('To jest American Express')
    else:
        print('Nieznany typ karty')

main()
