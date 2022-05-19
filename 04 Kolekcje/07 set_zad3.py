# Utwórz 2 krotki.
# Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki, a oraz nieparzystych elementów z drugiej.
# Przekształć powstałą listę w set.

krotka1 = (1, 2, 3, 4, 5, 'a', 'b')
krotka2 = ('a', 'b', 'c', 'd', 'e', 1, 2, 3)

krotka1_mod = krotka1[::2]
krotka2_mod = krotka2[1::2]

lista1 = krotka1_mod + krotka2_mod
print (lista1)

set1 = set(lista1)
print(set1)

