# Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def max_of_two(val1, val2):
    return val1 if val1 >= val2 else val2

# to samo rozpisane inaczej
    #     if val1 >= val2:
    #         return val1
    #     else:
    #         return val2


def maximum_of(a, b, c):
    return max_of_two(c, max_of_two(a, b))

# to samo rozpisane inaczej
    # max_ab = max_of_two(a, b)
    # max_abc = max_of_two(c, max_ab)
    # return max_abc


def main():
    a = input('Podaj 1 liczbę: ')
    b = input('Podaj 2 liczbę: ')
    c = input('Podaj 3 liczbę: ')

    result = maximum_of(a, b, c)

    print(result)


main()
