# tworzenie kopii listy
import copy

lista_1 = ['sam', 'frodo', 'pippin', "marry"]
lista_2 = lista_1.copy()
print(lista_2)
lista_21 = lista_1
print(lista_21)
lista_22 = copy.deepcopy(lista_1)
print(lista_22)

# sortowanie listy
    # w innej zmiennej
lista_3 = sorted(lista_1)
print(lista_3)
    # w miejscu
lista_2.sort()
print(lista_2)

# usuwanie elementów z listy
lista_2.clear()
print(lista_2)

# liczenie wystąpień elementu na liście
print(lista_1.count("sam"))

# sumowane liczb na liście
lista_4 = [1, 2, 3, 4, 5]
print(sum(lista_4))
