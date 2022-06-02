#  Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

# Wprowadzanie n numerów na listę
lista = []
print("Wprowadż 10 numerów")
for number in range(0, 10):
    new_number = int(input(f'{number+1} ->'))
    lista.append(new_number)

print("podane liczby to: ", lista)

# Sprawdzenie czy numery są parzyste i dodawanie do nowej listy
lista_parzysta = []
for i in lista:
    if i % 2 == 0:
        lista_parzysta.append(i)

print("Liczby parzyste na podanej liście to: ", lista_parzysta)
