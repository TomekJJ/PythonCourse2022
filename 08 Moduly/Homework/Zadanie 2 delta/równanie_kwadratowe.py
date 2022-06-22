import math

from delta import calculate_delta

def import_data():
    a = float(input('Podaj współczynnik a'))
    b = float(input('Podaj współczynnik b'))
    c = float(input('Podaj współczynnik c'))
    return a, b, c


def show_equation(a, b, c):
    print(f'Twoje równanie to: {a}x^2 + {b}x + {c} = 0')


def solve_equation(a, b, c):
    if calculate_delta(a, b, c) > 0:
        x1 = (-b - math.sqrt(calculate_delta(a,b,c))) / 2 * a
        x2 = (-b + math.sqrt(calculate_delta(a,b,c))) / 2 * a
        print(f'równanie ma dwa rozwiązania: {x1} oraz {x2}')
        print(x1)
        print(x2)
    elif calculate_delta(a, b, c) == 0:
        x = -b / 2 * a
        print(f'równanie ma jedno rozwiązanie: {x}')
    else:
        print("Równanie nie ma rozwiązań")

def main():
    a, b, c = import_data()
    show_equation(a, b, c)

    solution = solve_equation(a, b, c)
    print(solution)


main()

