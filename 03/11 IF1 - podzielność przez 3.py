# Poproś użytkownika o podanie liczby.
# Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

number = int(input("podaj liczbę całkowitą ->"))

if number % 3 == 0:
    print("twoja liczba jest podzielna przez 3")
else:
    print("twoja liczba nie jet podzielna przez 3 ")
