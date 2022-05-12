print('Czy 23 + 3 będzie się równać 15 + 12 ?')
print(23 + 3 == 15 + 12)
print('Czy dzielenie 29 przez 7 bez reszty wynosi 5?')
print(29 // 7 == 5)
print('Czy 27 podzielone przez 8 daje resztę 3?')
print(27 % 8 == 3)
liczba = input('podaj liczbę')
liczba = int(liczba)

# f string pozwala w princie dawać wartości zmiennych
print(f'czy liczba {liczba} jest parzysta?')
print(liczba % 2 == 0)
