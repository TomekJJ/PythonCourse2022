# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”'''

num1 = int(input('podaj pierwszą liczbę całkowitą ->'))
num2 = int(input('podaj drugą liczbę całkowitą ->'))

if num1 + num2 > 100:
    print(num1 + num2)
else:
    print('Koniec')



