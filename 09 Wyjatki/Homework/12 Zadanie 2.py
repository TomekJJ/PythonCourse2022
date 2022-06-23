# Utwórz dowolną krotkę zawierającą kilka wartości np. 10.
# Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd

krotka = (1, 2, 3, 4, 5, 6, 7)
print(f'oryginalny ciąg: {krotka}')

indeks = int(input("podaj indeks"))
value =  float(input ('podaj wartość'))

try:
    krotka[indeks] = value

except TypeError:
    print("Nie mogę wykonać")
    print(f'oryginalny ciąg: {krotka}')


