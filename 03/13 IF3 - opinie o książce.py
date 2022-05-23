# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
# Oblicz średnią opinię o książce.
# W zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

opinia1 = int(input('Opinia 1 ->'))
opinia2 = int(input('Opinia 2 ->'))
opinia3 = int(input('Opinia 3 ->'))

srednia = (opinia1 + opinia2 + opinia3) / 3

if srednia > 7:
    print('książka bardzo dobra')
elif srednia >= 5:
    print('ksiązka przeciętna')
else:
    print('książka nie warta uwag')
