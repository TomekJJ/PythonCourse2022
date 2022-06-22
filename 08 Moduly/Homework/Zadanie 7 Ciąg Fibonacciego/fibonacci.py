import math

def give_fibonacci (n):
    fibonacci = []
    if n == 0:
        fibonacci.append(0)
    elif n == 1:
        fibonacci.append(0)
        fibonacci.append(1)
    elif n == 2:
        fibonacci.append(0)
        fibonacci.append(1)
        fibonacci.append(1)
    elif n > 2:
        fibonacci = [0, 1, 1]
        for i in range(3, n):
            f_n = int(1 / math.sqrt(5) * ((1 + math.sqrt(5)) / 2)**i - 1 / math.sqrt(5) * ((1 - math.sqrt(5)) / 2)**i)
            fibonacci.append(f_n)
    return fibonacci


def give_fibonacci2 (n):
    fibonacci = [0 , 1]
    for i in range(2, n):
        f_n = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(f_n)
    return fibonacci


def main():
    n = int(input('give n: '))
    print(give_fibonacci(n))
    print(give_fibonacci2(n))

main()