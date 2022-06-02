# Użytkownik podaje dowolną liczbę N.
# Napisz kod, który wygeneruje słownik, wg zasady, że każdej liczbie przyporządkowany jest jej kwadrat (n : n * n).
    # Załóżmy, że użytkownik podał N = 8
    # Wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n = int(input("podaj jakąś liczbę -> "))

dict_sqr = {}

for v in range(1, n + 1):
    # print(f'kwadrat n: ', v * v)
    dict_sqr[v] = v * v

print(dict_sqr)