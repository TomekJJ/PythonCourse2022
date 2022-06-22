# Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

krotka = ("tomek", "andrzej", "monika", 71, "ola", "henio", "kazio", "ola", 71, "tomek")
lista_powt = []

lenght = len(krotka)

for i in range(0, lenght):
    if krotka.count(krotka[i]) > 1:
        if krotka[i] not in lista_powt:
            lista_powt.append(krotka[i])

print(krotka)
print("Powtarzające się wyrazy to: ", lista_powt)

# inaczej (z wykorzystaniem set)
print('....................')
print("Powtarzające się wyrazy to: ", set(lista_powt))


