# Napisz kod, który zwraca sumę wszystkich wielokrotności 5 lub 7 poniżej liczby N.
# Na przykład dla 21 mamy: 5, 7, 10, 14, 15, 20, stąd wynik 71

def find_multiple(a, n):
    multiples = []

    for i in range (1, n):
        if i * a < n:
            multiples.append(i * a)

    return multiples # (5, 10, 15, 20)

def main():
    a = int(input('a -> '))
    b = int(input('b -> '))
    n = int(input('n -> '))

    multiples = find_multiple(a, n) + find_multiple(b, n)
    sum_of_multiples = 0
    for v in multiples:
        sum_of_multiples += v

    print(sum_of_multiples)


main()