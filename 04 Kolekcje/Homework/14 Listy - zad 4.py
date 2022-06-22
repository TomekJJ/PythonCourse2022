# Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same

# Wprowadzanie elementów na listę
lista = []
print("Wprowadż parzystą liczbę elementów")
for i in range(0, 4):
    new_elem = input(f'{i + 1} -> ')
    lista.append(new_elem)

print("Twoja lista elementów to: ", lista)

# porównywanie środkowych elementów
lenght = len(lista)

if lista[int(lenght/2 - 1)] == lista[int(lenght / 2)]:
    print("Środkowe elementy są takie same")
