# Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę.
# Wyświetl liczby od największej do najmniejszej.

# x = int(input('Podaj pierwszą liczbę --> '))
# y = int(input('Podaj drugą liczbę --> '))
# z = int(input('Podaj trzecią liczbę --> '))
x = 5
y = 40
z = 3

# z listą
print("największa liczba to ", max(x, y, z))
lista = [x, y, z]
print('Posortowane liczby to: ', sorted(lista, key=None, reverse=True))

# z ifami
print('...................')

a = max(x, y, z)

if a == x and y >= z:
    print(a, y, z)
elif y <= z:
    print(a, z, y)

if a == y and x >= z:
    print(a, x, z)
elif x <= z:
    print(a, z, x)

if a == z and x >= y:
    print(a, x, y)
elif x >= y:
    print(a, y, x)

