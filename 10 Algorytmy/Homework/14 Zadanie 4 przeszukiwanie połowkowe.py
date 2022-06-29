# Napisz funkcję przeszukiwania połówkowego (binarenego), która przyjmuje dwa parametry - szukany element oraz listę elementów.
# Zwraca informację czy element jest obecny na liście, albo nie.

def find_binary(elem, data):
    if not elem in data:
        print("Szukanej liczby nie ma w przeszukiwanej tablicy!")

    data = sorted(data)
    left = 0
    right = len(data)

    while (left <= right):
       middle = (left + right) // 2

       if data[middle] < elem:
           left = middle + 1
       elif data[middle] > elem:
           right = middle
       else:
           print(f'szukana liczba znajduje się w zestawie pod indeksem {middle} (licząc od zera)')
           break


data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
elem = 2
print(sorted(data))

find_binary(elem, data)
