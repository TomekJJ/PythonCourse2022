'''
Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
    1. Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
    2. Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
    3. Połącz dane w jeden ciąg book za pomocą spacji
    4. Policz liczbę wszystkich znaków w napisie book
'''

# zapytanie
tytul = input("Podaj tytuł książki: ")
nazwisko = input("Podaj nazwisko autora książki: ")
strony = input("Podaj liczbę stron książki: ")

# 1. sprawdzenie zgodności
print('\n')
print(f'poprawność tytułu ', tytul.isalpha())
print(f'poprawność nazwiska ', nazwisko.isalpha())
print(f'poprawność liczby stron ', strony.isdigit())

# 2. zmiana wielkości liter

pierwsza_tytul = tytul[0]
tytul_mod = pierwsza_tytul.upper() + tytul[1:]

pierwsza_nazwisko = nazwisko[0]
nazwisko_mod = pierwsza_nazwisko.upper() + nazwisko[1:]

# 3 łączenie stringa
print('\n')
book = tytul_mod + ' ' + nazwisko_mod + ' ' + strony

print(book)
print(f'liczba znaków w opisie wynosi ', len(book))
