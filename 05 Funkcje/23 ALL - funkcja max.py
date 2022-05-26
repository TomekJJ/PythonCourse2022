# Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def maximum_of(a,b,c):
    if a >= b >= c:
        return a
    elif a >= c >= b:
        return a
    elif b >= a >= c:
         return b
    elif b >= c >= a:
        return b
    elif c >= a >= b:
        return c
    elif c >= b >= a:
        return c

def maximum_of2(a,b,c):
    if a >=b and a>=c:
        return a
    elif b>= a and b>=c:
        return b
    else:
        return c

def main():
    a = input('Podaj 1 liczbę: ')
    b = input('Podaj 2 liczbę: ')
    c = input('Podaj 3 liczbę: ')

    result = maximum_of(a,b,c)
    print(result)

    result2 = maximum_of2(a,b,c)
    print(result2)

main()