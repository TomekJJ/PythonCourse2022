# Stwórz grę ciepło zimno.
# Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf.
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz.
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random

# komputer
komp = random.randint(1,100)
print(komp)

# user
user = int(input('Podaj liczbę od 1 do 100 ->'))

i = 1
for i in range(1,7):
    if i >= 6:
        print("przegrałeś")
        break
    elif user == komp:
        print('wygrałeś')
        break
    elif komp > user:
        print('za mała liczba')
        user = int(input('Podaj liczbę od 1 do 100 ->'))
    elif user > komp:
        print('za duża liczba')
        user = int(input('Podaj liczbę od 1 do 100 ->'))

