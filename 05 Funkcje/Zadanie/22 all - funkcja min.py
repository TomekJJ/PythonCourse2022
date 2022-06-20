def maximum_of(a, b, c):
    if a <= b and a <= c:
        return a
    if b <= a and b <= c:
        return b
    else:
        return c


def main():
    a = input('podaj pierwszą liczbę: ')
    b = input('podaj drugą liczbę: ')
    c = input('podaj trzecią liczbę: ')

    result = maximum_of(a, b, c)
    print(f'Najmnieszja liczba to: {result}')


main()
