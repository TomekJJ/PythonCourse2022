# Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

lista1 = input("podaj liczby oddzielane przecinkami ->")
lista1 = lista1.split(', ')
print(lista1)

print(type(lista1))
print('Czy pierwszy i ostatni element są takie same?', lista1[0] == lista1[-1])

# innym sposobem to samo...
print("...........")

lista_10 = []
new_input = int(input("Wprowadć 10 numerów"))

for number in range(0, 10):
    new_number = int(input())
    lista_10.append(new_number)

print(lista_10)
print(lista_10[0] == lista_10[9])

