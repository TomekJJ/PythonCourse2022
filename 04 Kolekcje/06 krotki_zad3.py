# Stwórz krotkę liczb całkowitych.
# Poproś użytkownika o podanie dowolnej liczby.
# Jeśli liczba znajduje się na krotce wyswietl jej indeks.

krotka = (1, 3, 5, 7, 9, 11)

num = input("podaj liczbę ->")

# sposób 1
for i, v in enumerate(krotka): # i to indeks, v to wartość
    if int(num) == v:
        print('znalazłem, pod indeksem: ', i)
        break
    else:
        print('nie znalazłem')

# sposób 2 - flag
print('...')
flag = False
for i in num:
    if int(num) == i:
        print('znalazłem')
        flag = True
        break
if not flag:
    print('nie ma takiej liczby')

# sposób 3
print('...')
if num in krotka:
        print('znalazłem, pod indeksem:', krotka.index(num))
else:
        print('nie ma takiej liczby')
