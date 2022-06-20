# Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def is_in_range(a, b, x):
    if x >= a and x <= b:
        print(f'liczba {x} znajduje się w zakresie od {a} do {b}')
    else:
        print(f'liczba {x} nie znajduje się w zakresie od {a} do {b}')


def main():
    a = float(input('podaj dolną wartość zakresu:  '))
    b = float(input('podaj górną wartość zakresu:  '))
    x = float(input('podaj liczę:  '))

    is_in_range(a, b, x)


main()
