def is_even(num):
    if num % 2 == 0:
        print("podanaliczba jest parzysta")
    else:
        print("podana liczba jest nieparzysta")

num1 = int(input("podaj liczbe -> "))

is_even(num1)